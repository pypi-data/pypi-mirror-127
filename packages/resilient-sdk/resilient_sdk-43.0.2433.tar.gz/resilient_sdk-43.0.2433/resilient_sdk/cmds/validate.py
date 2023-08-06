#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

""" Implementation of `resilient-sdk validate` """

import logging
import os
import re

from resilient import ensure_unicode
from resilient_sdk.cmds.base_cmd import BaseCmd
from resilient_sdk.util import constants
from resilient_sdk.util import package_file_helpers as package_helpers
from resilient_sdk.util import sdk_helpers
from resilient_sdk.util import \
    sdk_validate_configs as validation_configurations
from resilient_sdk.util.sdk_exception import SDKException
from resilient_sdk.util.sdk_validate_issue import SDKValidateIssue

# Get the same logger object that is used in app.py
LOG = logging.getLogger(constants.LOGGER_NAME)

SUB_CMD_VALIDATE = ("--validate", )
SUB_CMD_TESTS = ("--tests", )
SUB_CMD_PYLINT = ("--pylint", )
SUB_CMD_BANDIT = ("--bandit", )
SUB_CMD_CVE = ("--cve", )
SUB_CMD_SELFTEST = ("--selftest", )


# optional parameters are skipped if they aren't included in the setup.py
SETUP_OPTIONAL_ATTRS = ("python_requires", "author_email")


class CmdValidate(BaseCmd):
    """TODO Docstring"""

    CMD_NAME = "validate"
    CMD_HELP = "Validate an App before packaging it"
    CMD_USAGE = """
    $ resilient-sdk validate -p <name_of_package>
    $ resilient-sdk validate -p <name_of_package> -c '/usr/custom_app.config'
    $ resilient-sdk validate -p <name_of_package> --validate
    $ resilient-sdk validate -p <name_of_package> --tests
    $ resilient-sdk validate -p <name_of_package> --pylint --bandit --cve --selftest"""
    CMD_DESCRIPTION = CMD_HELP
    CMD_ADD_PARSERS = ["app_config_parser"]

    VALIDATE_ISSUES = {}
    SUMMARY_LIST = []

    def setup(self):
        # Define codegen usage and description
        self.parser.usage = self.CMD_USAGE
        self.parser.description = self.CMD_DESCRIPTION
        
        # output not suppressed by default
        self.output_suppressed = False

        # Add any positional or optional arguments here
        self.parser.add_argument(constants.SUB_CMD_PACKAGE[1], constants.SUB_CMD_PACKAGE[0],
                                 type=ensure_unicode,
                                 required=True,
                                 help="(required) Path to existing package")

        self.parser.add_argument(SUB_CMD_VALIDATE[0],
                                 action="store_true",
                                 help="Run validation of package files")

        self.parser.add_argument(SUB_CMD_TESTS[0],
                                 action="store_true",
                                 help="Run tests using package's tox.ini file in a Python 3.6 environment")

        self.parser.add_argument(SUB_CMD_PYLINT[0],
                                 action="store_true",
                                 help="Run a pylint scan of all .py files under package directory (if 'pylint' is installed")

        self.parser.add_argument(SUB_CMD_BANDIT[0],
                                 action="store_true",
                                 help="Run a bandit scan of all .py files under package directory (if 'bandit' is installed")

        self.parser.add_argument(SUB_CMD_CVE[0],
                                 action="store_true",
                                 help="Run a safety scan of all .py files under package directory (if 'safety' is installed")

        self.parser.add_argument(SUB_CMD_SELFTEST[0],
                                 action="store_true",
                                 help="Validate and run the selftest.py file in the package directory (if 'resilient-circuits' and the package are installed in python environment)")

    def execute_command(self, args, output_suppressed=False):
        """
        TODO: docstring, unit tests
        """
        self.output_suppressed = output_suppressed
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Running validate on '{1}'".format(
            constants.LOG_DIVIDER, os.path.abspath(args.package)
        ))
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "Running with '{3}={1}', timestamp: {2}{0}".format(
            constants.LOG_DIVIDER, sdk_helpers.get_resilient_sdk_version(), 
            sdk_helpers.get_timestamp(), constants.SDK_PACKAGE_NAME
        ))

        self._print_package_details(args)

        sdk_helpers.is_python_min_supported_version()

        if not args.validate and not args.tests and not args.pylint and not args.bandit and not args.cve and not args.selftest:
            SDKException.command_ran = "{0} {1} | {2}".format(self.CMD_NAME, constants.SUB_CMD_PACKAGE[0], constants.SUB_CMD_PACKAGE[1])
            self._run_main_validation(args, )

        if args.validate:
            SDKException.command_ran = "{0} {1}".format(self.CMD_NAME, SUB_CMD_VALIDATE[0])
            self._validate(args, )

        if args.tests:
            SDKException.command_ran = "{0} {1}".format(self.CMD_NAME, SUB_CMD_TESTS[0])
            self._run_tests(args, )

        if args.pylint:
            SDKException.command_ran = "{0} {1}".format(self.CMD_NAME, SUB_CMD_PYLINT[0])
            self._run_pylint_scan(args, )

        if args.bandit:
            SDKException.command_ran = "{0} {1}".format(self.CMD_NAME, SUB_CMD_BANDIT[0])
            self._run_bandit_scan(args, )

        if args.cve:
            SDKException.command_ran = "{0} {1}".format(self.CMD_NAME, SUB_CMD_CVE[0])
            self._run_cve_scan(args, )

        if args.selftest:
            SDKException.command_ran = "{0} {1}".format(self.CMD_NAME, SUB_CMD_SELFTEST[0])
            self._run_selftest(args, )

        self._print_summary(self.SUMMARY_LIST)

    def _run_main_validation(self, args):
        """
        TODO: docstring, unit tests
        """
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Running main validation{0}".format(constants.LOG_DIVIDER))
        self._validate(args)
        self._run_selftest(args)


    def _print_package_details(self, args):
        """
        Print to the console the package details of the specified package
        including:
        - the absolute path of the package
        - display name of the package
        - name of the package
        - version of the package
        - version of SOAR the app was developed against
        - the python dependencies the app has
        - the description of the package
        - the name and email address of the developer
        - if the package supports resilient-circuits>=42.0, indicating that it is proxy supported or not

        :param args: command line args
        :type args: dict
        :return: None - adds list for VALIDATE_ISSUES["details"] in format [{attr1: attr_value}, {...: ...}, ...]
        :rtype: None
        """
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Printing details{0}".format(constants.LOG_DIVIDER))

        # list of string for output
        package_details_output = []
        # skips are skipped in non-DEBUG outputs as they are all considered too
        # long for normal output
        skips = ("long_description", "entry_points")

        # Get absolute path to package
        path_package = os.path.abspath(args.package)
        self._log(constants.VALIDATE_LOG_LEVEL_DEBUG, "Path to project: {0}".format(path_package))

        # Ensure the package directory exists and we have READ access
        sdk_helpers.validate_dir_paths(os.R_OK, path_package)
        # Generate path to setup.py file + validate we have permissions to read it
        path_setup_py_file = os.path.join(path_package, package_helpers.BASE_NAME_SETUP_PY)
        sdk_helpers.validate_file_paths(os.R_OK, path_setup_py_file)



        # parse all supported attributes from setup.py
        parsed_setup_file = package_helpers.parse_setup_py(path_setup_py_file, package_helpers.SUPPORTED_SETUP_PY_ATTRIBUTE_NAMES)

        # check through setup.py file parse 
        # (including values that are in 'skips' here, though they will not be output at the end of this method)
        for attr in package_helpers.SUPPORTED_SETUP_PY_ATTRIBUTE_NAMES:
            attr_val = parsed_setup_file.get(attr)

            # optional parameters are skipped if their values aren't found
            if attr_val or attr not in SETUP_OPTIONAL_ATTRS:
                package_details_output.append({attr: attr_val if attr_val else "**NOT FOUND**"})



        # parse import definition from export.res file or from customize.py (deprecated)
        # package_helpers.get_import_definition_from_customize_py will raise an SDKException if there is an error
        # getting the customize.py file or the import definition from that file
        # we catch this error and output a message that the customize.py file was not correctly found
        try:
            path_customize_py = os.path.join(path_package, parsed_setup_file.get("name"), package_helpers.PATH_CUSTOMIZE_PY)
            sdk_helpers.validate_file_paths(os.R_OK, path_customize_py)
            import_definition = package_helpers.get_import_definition_from_customize_py(path_customize_py)
            if import_definition.get("server_version", {}).get("version"):
                package_details_output.append({"SOAR version": import_definition.get("server_version").get("version")})
            else:
                package_details_output.append({"SOAR version": "Not specified in 'util/data/export.res'. Reload code to make sure server_version is set."})
        except SDKException as e:
            package_details_output.append({"SOAR version": "**NOT FOUND**; customize.py file not found in {0}".format(path_customize_py)})
            


        # proxy support is determined by the version of resilient-circuits that is installed
        # if version 42 or greater, proxies are supported
        library_found = False
        for package in parsed_setup_file.get("install_requires"):
            if re.findall(r"(?:resilient[\-,\_]circuits\>\=)([0-9]+\.[0-9]+\.[0-9]+)", package):
                circuits_version = re.findall(r"[0-9]+", package)
                circuits_version = tuple([int(i) for i in circuits_version])

                package_details_output.append({"Proxy support": "Proxies supported if running on AppHost>=1.6" if circuits_version >= constants.RESILIENT_VERSION_WITH_PROXY_SUPPORT else "Proxies not fully supported unless running on AppHost>=1.6 and resilient-circuits>=42.0.0"})
                library_found = True
                break
        if not library_found:
            package_details_output.append({"install_requires.resilient_circuits": "'resilient_circuits' not found in 'install_requires' in package's setup.py"})



        # print output
        for attr_dict in package_details_output:
            for attr in attr_dict:
                if attr not in skips:
                    level = constants.VALIDATE_LOG_LEVEL_INFO
                else:
                    level = constants.VALIDATE_LOG_LEVEL_DEBUG
                self._log(level, u"{0}: {1}".format(attr, attr_dict[attr]))



        # append details to VALIDATE_ISSUES["details"]
        # details don't count toward final counts so they don't get
        # appended to SUMMARY_LIST
        self.VALIDATE_ISSUES["details"] = package_details_output

    def _validate(self, args):
        """
        TODO: unit tests once all validations are written
        Run static validations.
        Wrapper method that validates the contents of the following files in the package dir (all called in separate submethods):
        - setup.py - done in _validate_setup()
        - MANIFEST.in - done in _validate_package_files()
        - apikey_permissions.txt - done in _validate_package_files()
        - entrypoint.sh - done in _validate_package_files()
        - Dockerfile - done in _validate_package_files()
        - fn_package/util/config.py - TBD
        - fn_package/util/customize.py - TBD
        - fn_package/util/selftest.py - TBD
        - fn_package/LICENSE - TBD
        - fn_package/icons - TBD
        - README.md - TBD

        :param args: list of args
        :type args: dict
        :raise SDKException: if the path to the package or required file is not found
        :return: None
        :rtype: None
        """

        # Get absolute path to package
        path_package = os.path.abspath(args.package)
        # Ensure the package directory exists and we have READ access
        sdk_helpers.validate_dir_paths(os.R_OK, path_package)
        self._log(constants.VALIDATE_LOG_LEVEL_DEBUG, "Path to project: {0}".format(path_package))


        # list of ("<file_name>", <validation_function>)
        # this list gets looped and each sub method is ran to check if file is valid
        validations = [
            ("setup.py", self._validate_setup),
            ("package files", self._validate_package_files)
        ]


        # loop through files and their associated validation functions
        for file_name, validation_func in validations:
            self._log(constants.VALIDATE_LOG_LEVEL_INFO, u"{0}Validating {1}{0}".format(constants.LOG_DIVIDER, file_name))

            # validate given file using static helper method
            file_valid, issues = validation_func(path_package)
            self.VALIDATE_ISSUES[file_name] = issues
            self.SUMMARY_LIST += issues

            # log output from validation
            for issue in issues:
                self._log(issue.get_logging_level(), issue.error_str())

            self._print_status(constants.VALIDATE_LOG_LEVEL_INFO, file_name, file_valid)


        # TODO: implement other static validates
        #       - fn_package/util/config.py
        #       - fn_package/util/customize.py
        #       - fn_package/LICENSE
        #       - fn_package/icons
        #       - README.md

    @staticmethod
    def _validate_setup(path_package):
        """
        Validate the contents of the setup.py file in the given package.
        Builds a list of SDKValidateIssue that describes the status of setup.py

        Uses the sdk_validate_configs.py util file to define the following checks:
        - CRITICAL: Check the file exists
        - CRITICAL: name: is all lowercase and only special char allowed is underscore
        - WARN: display_name: check does not start with <<
        - CRITICAL: license: check does not start with << or is none of any of the GPLs
        - CRITICAL: author: does not start with <<
        - CRITICAL: author_email: does not include "@example.com"
        - CRITICAL: description: does start with default "Resilient Circuits Components"
        - CRITICAL: long_description: does start with default "Resilient Circuits Components"
        - CRITICAL: install_requires: includes resilient_circuits or resilient-circuits at a minimum
        - WARN: checks if exists and WARNS the user if not "python_requires='>=3.6'"
        - CRITICAL: entry_points: that .configsection, .customize, .selftest

        :param path_package: path to package
        :type path_package: str
        :return: Returns boolean value of whether or not the run passed and a sorted list of SDKValidateIssue
        :rtype: (bool, list[SDKValidateIssue])
        """
        
        # empty list of SDKValidateIssues
        issues = []
        # boolean to determine if setup passes validation
        setup_valid = True



        # Generate path to setup.py file + validate we have permissions to read it
        path_setup_py_file = os.path.join(path_package, package_helpers.BASE_NAME_SETUP_PY)
        sdk_helpers.validate_file_paths(os.R_OK, path_setup_py_file)
        LOG.debug("setup.py file found at path {0}\n".format(path_setup_py_file))



        attributes = validation_configurations.setup_py_attributes

        # check through setup.py file parse
        for attr in attributes:
            attr_dict = attributes.get(attr)

            # get output details from attr_dict (to be modified as necessary based on results)
            fail_func = attr_dict.get("fail_func")
            severity = attr_dict.get("severity")
            fail_msg = attr_dict.get("fail_msg")
            missing_msg = attr_dict.get("missing_msg")
            solution = attr_dict.get("solution")

            # run given parsing function
            parsed_attr = attr_dict.get("parse_func")(path_setup_py_file, [attr]).get(attr)

            # check if attr is missing from setup.py file
            if not parsed_attr:
                # if attr isn't found and it is optional, skip to the next attr
                if attr in SETUP_OPTIONAL_ATTRS:
                    continue
                
                name = "{0} not found".format(attr)
                description = missing_msg.format(attr)
            elif fail_func(parsed_attr): # check if it fails the 'fail_func'
                formats = [attr, parsed_attr]

                # some attr require a supplemental lambda function to properly output their failure message
                if attr_dict.get("fail_msg_lambda_supplement"):
                    formats.append(attr_dict.get("fail_msg_lambda_supplement")(parsed_attr))

                name = "invalid value in setup.py"
                description = fail_msg.format(*formats)
            else: # else is present and did not fail
                # passes checks
                name = "{0} valid in setup.py".format(attr)
                description = u"'{0}' passed".format(attr)
                severity = SDKValidateIssue.SEVERITY_LEVEL_DEBUG
                solution = "Value found for '{0}' in setup.py: '{1}'"

            # for each attr create a SDKValidateIssue to be appended to the issues list
            issue = SDKValidateIssue(
                name,
                description,
                severity=severity,
                solution=solution.format(attr, parsed_attr)
            )

            issues.append(issue)

        issues.sort()

        # determine if setup validation has failed
        # the any method will short circuit once the condition evaluates to true at least once
        # and then flip the value to indicate whether or not the validation passed
        setup_valid = not any(issue.severity == SDKValidateIssue.SEVERITY_LEVEL_CRITICAL for issue in issues)
        
        return setup_valid, issues

    @staticmethod
    def _validate_package_files(path_package):
        """
        Validate the contents of the following files:
        - apikey_permissions.txt
        - MANIFEST.in
        - Dockerfile
        - entrypoint.sh
        
        It validates first that each file exists.
        If the file doesn't exist, issue with CRITICAL is created
        If the file exists, check the validation of that given file by running the given "func" for it

        :param path_package: path to package
        :type path_package: str
        :return: Returns boolean value of whether or not the run passed and a sorted list of SDKValidateIssue
        :rtype: (bool, list[SDKValidateIssue])
        """
        # empty list of SDKValidateIssues
        issues = []
        # boolean to determine if package_files passes validation
        package_files_valid = True


        # get package name and package version
        parsed_setup = package_helpers.parse_setup_py(os.path.join(path_package, package_helpers.BASE_NAME_SETUP_PY), ["name", "version"])
        package_name = parsed_setup.get("name")
        package_version = parsed_setup.get("version")

        # run through validations for package files
        # details of each check can be found in the sdk_validate_configs.package_files
        for filename in validation_configurations.package_files:
            attr_dict = validation_configurations.package_files.get(filename)

            # if a specific path is required for this file, it will be specified in the "path" attribute
            if attr_dict.get("path"):
                path_file = os.path.join(path_package, attr_dict.get("path").format(package_name))
            else:
                # otherwise the file is in root package directory
                path_file = os.path.join(path_package, filename)

            # check that the file exists
            try: 
                sdk_helpers.validate_file_paths(os.R_OK, path_file)
                LOG.debug("{0} file found at path {1}\n".format(filename, path_file))
            except SDKException:
                # file not found: create issue with given "missing_..." info included
                issue_list = [SDKValidateIssue(
                    name=attr_dict.get("missing_name"),
                    description=attr_dict.get("missing_msg").format(path_file),
                    severity=attr_dict.get("missing_severity"),
                    solution=attr_dict.get("missing_solution").format(path_package)
                )]
            else: # SDKException wasn't caught -- the file exists!

                # make sure the "func" param is specified
                if not attr_dict.get("func"):
                    raise SDKException("'func' not defined in attr_dict={0}".format(attr_dict))

                # run given "func"
                issue_list = attr_dict.get("func")(
                    filename=filename,
                    attr_dict=attr_dict,
                    package_version=package_version,
                    package_name=package_name,
                    path_file=path_file,
                    path_package=path_package
                )

            issues.extend(issue_list)


        # sort and look for and invalid issues
        issues.sort()
        package_files_valid = not any(issue.severity == SDKValidateIssue.SEVERITY_LEVEL_CRITICAL for issue in issues)

        return package_files_valid, issues

    @staticmethod
    def _validate_selftest(path_package, args):
        """
        Validate the contents of the selftest.py file in the given package:
        - check if the package resilient-circuits>=42.0.0 is installed on this Python environment 
          and WARN the user that it is not installed, tell them how to get it
        - verify that this package is installed
        - verify that a util/selftest.py file is present
        - verify that unimplemented does not exist in the file
        - run the selftest method

        :param path_package: path to the package
        :type path_package: str
        :return: Returns boolean value of whether or not the run passed and a sorted list of SDKValidateIssue
        :rtype: (bool, list[SDKValidateIssue])
        """

        # empty list of SDKValidateIssues
        issues = []
        # boolean to determine if selftest passes validation
        selftest_valid = True


        # Generate path to selftest.py file + validate we have permissions to read
        # note that file validation happens in the validations list
        package_name = package_helpers.parse_setup_py(os.path.join(path_package, package_helpers.BASE_NAME_SETUP_PY), ["name"]).get("name")
        path_selftest_py_file = os.path.join(path_package, package_name, package_helpers.PATH_SELFTEST_PY)
        LOG.debug("selftest.py file found at path {0}\n".format(path_selftest_py_file))


        # run through validations for selftest
        # details of each check can be found in the sdk_validate_configs.py.selftest_attributes
        for attr_dict in validation_configurations.selftest_attributes:
            if not attr_dict.get("func"):
                raise SDKException("'func' not defined in attr_dict={0}".format(attr_dict))
            issue_passes, issue = attr_dict.get("func")(
                attr_dict=attr_dict,
                path_selftest_py_file=path_selftest_py_file,
                package_name=package_name,
                path_package=path_package,
                path_app_config=args.config
            )
            issues.append(issue)
            if not issue_passes:
                issues.sort()
                return False, issues


        # sort and look for and invalid issues
        issues.sort()
        selftest_valid = not any(issue.severity == SDKValidateIssue.SEVERITY_LEVEL_CRITICAL for issue in issues)

        return selftest_valid, issues

    def _run_tests(self, args):
        """
        TODO
        """
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Running tests{0}".format(constants.LOG_DIVIDER))

    def _run_pylint_scan(self, args):
        """
        TODO
        """
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Running pylint{0}".format(constants.LOG_DIVIDER))

    def _run_bandit_scan(self, args):
        """
        TODO
        """
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Running bandit{0}".format(constants.LOG_DIVIDER))

    def _run_cve_scan(self, args):
        """
        TODO
        """
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Running safety{0}".format(constants.LOG_DIVIDER))

    def _run_selftest(self, args):
        """
        Validates and executes selftest.py
        """
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Validating selftest.py{0}".format(constants.LOG_DIVIDER))


        # Get absolute path to package
        path_package = os.path.abspath(args.package)
        # Ensure the package directory exists and we have READ access
        sdk_helpers.validate_dir_paths(os.R_OK, path_package)

        # validate selftest.py and then execute it if valid
        file_valid, issues = self._validate_selftest(path_package, args)
        self.VALIDATE_ISSUES["selftest.py"] = issues
        self.SUMMARY_LIST += issues

        for issue in issues:
            self._log(issue.get_logging_level(), issue.error_str())

        self._print_status(constants.VALIDATE_LOG_LEVEL_INFO, "selftest.py", file_valid)




    def _print_summary(self, static_issues_list):
        """
        From list of issues, generates a count of issues that are CRITICAL, WARNING, PASS=sum(INFO, DEBUG)
        and outputs in the format:

        ------------------------
        Validation Results
        ------------------------

        Critical Issues:     <counts[critical]>
        Warnings:            <counts[warning]>
        Validations Passed:  <counts[pass]>

        ------------------------

        :param issues_list: list of SDKValidateIssue objects
        :type issues_list: list[SDKValidateIssue]
        :return: None - prints output to console
        :rtype: None
        """
        counts = {
            SDKValidateIssue.SEVERITY_LEVEL_CRITICAL: 0,
            SDKValidateIssue.SEVERITY_LEVEL_WARN: 0,
            SDKValidateIssue.SEVERITY_LEVEL_INFO: 0,
            SDKValidateIssue.SEVERITY_LEVEL_DEBUG: 0,
        }
        for issue in static_issues_list:
            counts[issue.severity] += 1
        
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "{0}Validation Results{0}".format(constants.LOG_DIVIDER))
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "Critical Issues: {0:>14}".format(
            package_helpers.color_output(counts[SDKValidateIssue.SEVERITY_LEVEL_CRITICAL], "CRITICAL")
        ))
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "Warnings: {0:>21}".format(package_helpers.color_output(counts[SDKValidateIssue.SEVERITY_LEVEL_WARN], "WARNING")))
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, "Validations Passed: {0:>11}".format(package_helpers.color_output(
            int(counts[SDKValidateIssue.SEVERITY_LEVEL_DEBUG]) + int(counts[SDKValidateIssue.SEVERITY_LEVEL_INFO]), "PASS")
        ))
        # self._log(constants.VALIDATE_LOG_LEVEL_INFO, "\nSee the detailed report at {0}".format("TODO")) # TODO
        self._log(constants.VALIDATE_LOG_LEVEL_INFO, constants.LOG_DIVIDER)

    def _print_status(self, level, msg, run_pass):
        """
        Class helper method for logging the status of a specific validation with formatting and color added in
        
        :param level: level to log (from constants.VALIDATE_LOG_LEVEL_<level>)
        :type level: str
        :param msg: message to be formatted and printed
        :type msg: str
        :param run_pass: indicates whether or not this specific validation has passed
        :type run_pass: bool
        :return: None - outputs to console using self._log
        :rtype: None
        """
        status = "PASS" if run_pass else "FAIL"
        msg_formatted = "{0}{1} {2}{0}".format(constants.LOG_DIVIDER, msg, status)
        msg_colored = package_helpers.color_output(msg_formatted, status)
        self._log(level, msg_colored)


    def _log(self, level, msg):
        """
        Class wrapper method for cleaner logging calls.
        Makes use of the class variable "output_suppressed" to calculate if validate
        output should be output to the console (allows for silent running in other sdk commands)
        """
        LOG.log(CmdValidate._get_log_level(level, self.output_suppressed), msg)

    @staticmethod
    def _get_log_level(level, output_suppressed=False):
        """
        Returns logging level to use with logger
        
        50=LOG.critical
        40=LOG.error
        30=LOG.warning
        20=LOG.info
        10=LOG.debug

        https://docs.python.org/3.6/library/logging.html#levels

        :param level: string value of DEBUG, INFO, WARNING, or ERROR; this value is used if output_suppressed==False
        :type level: str
        :param output_suppressed: (optional) value to suppress output; designed for use when calling validate 
                                  from another sdk cmd when output is suppressed, DEBUG level is returned
        :type output_suppressed: bool
        :return: value corresponding to the appropriate log level
        :rtype: int
        """
        if output_suppressed:
            return 10

        if not isinstance(level, str):
            return 10

        level = level.upper()

        if level == constants.VALIDATE_LOG_LEVEL_DEBUG:
            return 10
        elif level == constants.VALIDATE_LOG_LEVEL_INFO:
            return 20
        elif level == constants.VALIDATE_LOG_LEVEL_WARNING:
            return 30
        if level == constants.VALIDATE_LOG_LEVEL_ERROR:
            return 40
        if level == constants.VALIDATE_LOG_LEVEL_CRITICAL:
            return 50
        
        # default returns 10==DEBUG
        return 10
