import os
from pathlib import Path

from click.termui import style

# Paths and file names

GLOBAL_RESOURCE_PATH = Path(os.path.expanduser("~/.bento"))
GLOBAL_CONFIG_PATH = GLOBAL_RESOURCE_PATH / "config.yml"
DEFAULT_LOG_PATH = GLOBAL_RESOURCE_PATH / "last.log"
VENV_PATH = GLOBAL_RESOURCE_PATH / "venv"
DEFAULT_GLOBAL_GIT_IGNORE_PATH = Path(os.path.expanduser("~/.config/git/ignore"))

RESOURCE_PATH = Path(".bento")
CACHE_PATH = Path("cache")

ARCHIVE_FILE_NAME = "archive.json"
CONFIG_FILE_NAME = "config.yml"
IGNORE_FILE_NAME = ".bentoignore"

GREP_CONFIG_FILE_NAME = "grep-config.yml"

# Registration data

TERMS_OF_SERVICE_KEY = "terms_of_service"
TERMS_OF_SERVICE_VERSION = "0.3.0"

# Identifiers

BENTO_TEMPLATE_HASH = "3a04e0f0cd9243d20b1e33da7ac13115"

BENTO_EMAIL_VAR = "BENTO_EMAIL"
BENTO_TEST_VAR = "BENTO_TEST"
QA_TEST_EMAIL_ADDRESS = "test@returntocorp.com"
SUPPORT_EMAIL_ADDRESS = "support@r2c.dev"

SLACK_SIGNUP_LINK = "https://join.slack.com/t/r2c-community/shared_invite/enQtNjU0NDYzMjAwODY4LWE3NTg1MGNhYTAwMzk5ZGRhMjQ2MzVhNGJiZjI1ZWQ0NjQ2YWI4ZGY3OGViMGJjNzA4ODQ3MjEzOWExNjZlNTA"

# Metrics constants

ARGS_TO_EXCLUDE_FROM_METRICS = {"check": {"paths"}}

### messages ###

UPGRADE_WARNING_OUTPUT = f"""
╭─────────────────────────────────────────────╮
│  🎉 A new version of Bento is available 🎉  │
│  Try it out by running:                     │
│                                             │
│       {style("pip3 install --upgrade bento-cli", fg="blue")}      │
│                                             │
╰─────────────────────────────────────────────╯
"""
