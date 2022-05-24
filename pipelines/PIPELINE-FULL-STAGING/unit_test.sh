#!/bin/bash

source todo-list-aws/bin/activate
set -x
# Create temporal environment variable PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
echo "PYTHONPATH: $PYTHONPATH"
# Create temporal environment variable DYNAMODB_TABLE
export DYNAMODB_TABLE=todoUnitTestsTable
# Pass unit test
python test/unit/TestToDo.py
# run test under coverage 
pip show coverage
coverage run --include=src/todoList.py test/unit/TestToDo.py
coverage report
coverage xml