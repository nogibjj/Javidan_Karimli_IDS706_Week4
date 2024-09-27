
[![CI Pipeline](https://github.com/nogibjj/Javidan_Karimli_IDS706_Week4/actions/workflows/main.yaml/badge.svg)](https://github.com/nogibjj/Javidan_Karimli_IDS706_Week4/actions/workflows/main.yaml)

# GitHub Actions: Matrix Build Across Python Versions

## Project Overview
This project aims to test multiple Python versions and configurations using GitHub Actions. The `setup-python` action is combined with a matrix strategy to run various jobs under different environments. The script `main.py` is used to detect the operating system and Python version for each job.

## Setup Instructions
1. Clone the repository.
2. Create a container environment or run make install to activate with the dependencies from `requirements.txt`.
3. Modify the code in `main.py` or `test_main.py` as needed.
4. Push changes to trigger tests across multiple OS and Python environments.

## Code Formatting and Error Checking
1. Format your code using `make format`.

![Format Run Example](https://github.com/nogibjj/Javidan_Karimli_IDS706_Week4/blob/1b144c960c6d8b927d08a821b0036da0f8071ea3/data/format.png)

2. Lint the code with `make lint`.

Example of linting errors:

![Lint Run Example](https://github.com/nogibjj/Javidan_Karimli_IDS706_Week4/blob/1b144c960c6d8b927d08a821b0036da0f8071ea3/data/lint.png)

3. Run tests using `make test`.

Example of test cases:

![Test Cases Example](https://github.com/nogibjj/Javidan_Karimli_IDS706_Week4/blob/1b144c960c6d8b927d08a821b0036da0f8071ea3/data/test.png)

## Matrix Strategy with GitHub Actions

![Matrix Build Example](https://github.com/nogibjj/Javidan_Karimli_IDS706_Week4/blob/1b144c960c6d8b927d08a821b0036da0f8071ea3/data/matrix_build.png)
