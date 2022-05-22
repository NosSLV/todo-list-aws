#!/bin/bash

# Access python virtual environment: todo-list-aws
source todo-list-aws/bin/activate
# Get all instructions displayed to the console
set -x
# Validate region before build
sam validate --region us-east-1
# Build the application
sam build
