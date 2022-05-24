#!/bin/bash

# Setup file for PRODUCTION STAGE

# Get all instructions displayed to the console
set -x
# Create virtual environment
python3.7 -m venv todo-list-aws
# Access python virtual environment: todo-list-aws
source todo-list-aws/bin/activate
# Install SAM CLI
python -m pip install --upgrade pip
python -m pip install awscli
python -m pip install aws-sam-cli
# For integration testing
python -m pip install pytest
# Show actual directory
pwd