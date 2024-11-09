# Ensure that the tests are run with proper virtual environment activation
if (-not (Test-Path ".venv")) {
    Write-Host "Please create a virtual environment before running the tests."
    exit 1
}

# Activate the virtual environment
. .venv\Scripts\Activate

# Run the tests and capture the output in the results.txt file
pytest --maxfail=5 --disable-warnings | Tee-Object -FilePath "output/results.txt"

# Deactivate the virtual environment
deactivate
