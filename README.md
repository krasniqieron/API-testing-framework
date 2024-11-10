
# Automation Test Framework

This framework provides an easy way to run automated tests for the CatFact API using Python. The tests cover a variety of API endpoints and parameters.

## Prerequisites
- **Python**: Version 3.6 or higher
- **pip**: Python package installer

## Steps to Run the Automation Framework

### Step 1: Clone the Repository
Clone the project repository to your local machine.

```bash
git clone https://github.com/krasniqieron/API-testing-framework.git
```

### Step 2: Create a Virtual Environment (Recommended)
Creating a virtual environment helps to isolate dependencies for this project.

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment
Activate the virtual environment to use the project's specific dependencies.

- **Windows (PowerShell)**:
  ```bash
  .venv\Scripts\Activate
  ```
- **MacOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### Step 4: Install Dependencies
Use the `requirements.txt` file to install all necessary dependencies.

```bash
pip install -r requirements.txt
```

### Step 5: Running the Tests

You can use the following scripts to run the tests based on your operating system:

- **Windows (PowerShell)**: `run_tests.ps1`
- **Linux/MacOS (Bash)**: `run_tests.sh`

#### Running on Windows (PowerShell)
```bash
powershell.exe ./run_tests.ps1
```

#### Running on Linux/MacOS (Bash)
```bash
bash ./run_tests.sh
```

### Step 6: Viewing the Results
After running the tests, the results will be saved in `output/results.txt`. To view the results, use:

```bash
cat output/results.txt
```

## Test Cases

The test suite includes the following API endpoint tests:

- **/fact**: Retrieves a single cat fact.
- **/facts**: Retrieves multiple cat facts.
- **/breeds**: Retrieves available cat breeds.
- **Parameters**: Some tests include parameters like `max_length` and `limit` for additional functionality.

### Framework Structure

- **tests/**: Contains the test scripts.
- **output/**: Stores test results in `results.txt`.
- **run_tests.sh**: Shell script for running tests on Linux/MacOS.
- **run_tests.ps1**: PowerShell script for running tests on Windows.

