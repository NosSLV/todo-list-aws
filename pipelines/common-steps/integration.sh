#!/bin/bash

# Access python virtual environment: todo-list-aws
source todo-list-aws/bin/activate
# Get all instructions displayed to the console
set -x
# Make temporal environment variable BASE_URL equal to variable defined in jenkinsfile
export BASE_URL=$1
# Using pytest to pass API integration test
pytest -s test/integration/todoApiTest.py