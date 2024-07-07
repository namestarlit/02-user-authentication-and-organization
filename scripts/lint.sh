#!/usr/bin/env bash
# check for linting errors in the app package
set -e
set -x

mypy app
ruff check app
ruff format app --check

