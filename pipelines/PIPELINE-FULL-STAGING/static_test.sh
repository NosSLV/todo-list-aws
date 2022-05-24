#!/bin/bash

# Access python virtual environment: todo-list-aws
source todo-list-aws/bin/activate
# Get all instructions displayed to the console
set -x

# Static Test RADON CC
RAD_ERRORS=$(radon cc src -nc | wc -l)
if [[ $RAD_ERRORS -ne 0 ]]
then
    echo 'Ha fallado el análisis estatico de RADON - CC'
    exit 1
fi
# Static Test RADON MI
RAD_ERRORS=$(radon mi src -nc | wc -l)
if [[ $RAD_ERRORS -ne 0 ]]
then
    echo 'Ha fallado el análisis estatico de RADON - MI'
    exit 1
fi

# Test flake8 in all python files
flake8 src/*.py
if [[ $? -ne 0 ]]
then
    exit 1
fi
# Test bandit in all python files
bandit src/*.py
if [[ $? -ne 0 ]]
then
    exit 1
fi