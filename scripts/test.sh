#!/usr/bin/env bash
# Run tests
set -e
set -x

coverage run --source=ulms -m pytest
coverage report --show-missing
coverage html --title "${@-coverage}"

