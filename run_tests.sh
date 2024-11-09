#!/bin/bash

# Ensure that the tests are run with proper virtual environment activation
if [ ! -d ".venv" ]; then
    echo "Please create a virtual environment before running the tests."
    exit 1
fi

# Activate the virtual environment
source .venv/bin/activate

# Run the tests and capture the output in the results.txt file
pytest --maxfail=5 --disable-warnings > output/results.txt; tail -n 20 output/results.txt

# Deactivate the virtual environment
deactivate
