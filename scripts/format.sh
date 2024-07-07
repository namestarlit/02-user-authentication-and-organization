#!/usr/bin/env bash
#Fomating and litting errors
set -e 
set -x

ruff check app scripts --fix
ruff format app scripts
