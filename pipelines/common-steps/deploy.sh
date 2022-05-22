#!/bin/bash

# Get all instructions displayed to the console
set -x
# Summarize file space usage of each file
du -hs * | sort -h
# Deploy application in variable ENVIRONMENT. Forcing upload even if the artifacts exists, return exit code 0 if no changes and no need of manual confirmation.
sam deploy template.yaml --config-env ${ENVIRONMENT} --no-confirm-changeset --force-upload --no-fail-on-empty-changeset --no-progressbar
