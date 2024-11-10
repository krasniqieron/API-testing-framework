#!/bin/bash

# Function to print and log messages to the output
log_message() {
    echo "$1"
    echo "$1" >> output/results.txt
}

# Function to activate the virtual environment
activate_venv() {
    log_message "Activating virtual environment..."
    # Check if the virtual environment exists
    if [ -d ".venv" ]; then
        source .venv/bin/activate  # For Linux/macOS
        log_message "Virtual environment activated."
    else
        log_message "Error: Virtual environment not found. Please create one by running 'python -m venv .venv'."
        exit 1
    fi
}

# Function to install dependencies (uncomment if you want this in the script)
install_dependencies() {
    log_message "Installing dependencies from requirements.txt..."
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        log_message "Dependencies installed successfully."
    else
        log_message "No requirements.txt found. Skipping dependency installation."
    fi
}

# Function to run tests
run_tests() {
    log_message "Running tests and capturing output in results.txt..."

    # Run pytest and capture the output in results.txt
    pytest tests --maxfail=5 --disable-warnings --capture=sys > output/results.txt

    if [ $? -eq 0 ]; then
        log_message "Tests passed successfully!"
    else
        log_message "Some tests failed. Check results.txt for details."
    fi
}

# Main script execution

# Clear old results
log_message "Clearing previous results in results.txt..."
> output/results.txt

# Activate virtual environment
activate_venv

# Install dependencies (uncomment if you want to install dependencies)
# install_dependencies

# Run the tests
run_tests

# Display the results to the user
log_message "Test run completed. Displaying results:"
cat output/results.txt
