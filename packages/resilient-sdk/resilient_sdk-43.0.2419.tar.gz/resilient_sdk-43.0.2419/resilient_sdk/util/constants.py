#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

LOGGER_NAME = "resilient_sdk_log"
LOG_DIVIDER = "\n------------------------\n"
ENV_VAR_DEV = "RES_SDK_DEV"
ENV_VAR_APP_CONFIG_FILE = "APP_CONFIG_FILE"

RESILIENT_LIBRARIES_VERSION = "43.0.0"
RESILIENT_LIBRARIES_VERSION_DEV = "43.0.0"
RESILIENT_VERSION_WITH_PROXY_SUPPORT = (42, 0, 0)
CURRENT_SOAR_SERVER_VERSION = 42

MIN_SUPPORTED_PY_VERSION = (3, 6)
SDK_PACKAGE_NAME = "resilient-sdk"
CIRCUITS_PACKAGE_NAME = "resilient-circuits"

SUB_CMD_PACKAGE = ("--package", "-p")

# Resilient export file suffix.
RES_EXPORT_SUFFIX = ".res"
# Endpoint url for importing a configuration
IMPORT_URL = "/configurations/imports"
# Path to package templates for jinja rendering
PACKAGE_TEMPLATE_PATH = "data/codegen/templates/package_template"
DOCGEN_TEMPLATE_PATH = "data/docgen/templates"


DOCGEN_PLACEHOLDER_STRING = "::CHANGE_ME::"

VALIDATE_LOG_LEVEL_CRITICAL = "CRITICAL"
VALIDATE_LOG_LEVEL_ERROR = VALIDATE_LOG_LEVEL_CRITICAL
VALIDATE_LOG_LEVEL_WARNING = "WARNING"
VALIDATE_LOG_LEVEL_INFO = "INFO"
VALIDATE_LOG_LEVEL_DEBUG = "DEBUG"
