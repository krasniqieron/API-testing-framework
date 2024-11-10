# Activate the virtual environment using the correct script for PowerShell
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate.ps1

# Clear the results.txt file to start fresh
Write-Host "Clearing previous results in results.txt..."
Clear-Content -Path ".\output\results.txt"

# Run pytest with the -s flag to capture print statements and redirect output to results.txt
Write-Host "Running tests and capturing output in results.txt..."
pytest -s > .\output\results.txt

# Display a message when done
Write-Host "Tests completed. Results saved in output/results.txt."
