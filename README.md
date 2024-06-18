# Jayjay_module_22

# Automation Testing Project

This repository contains automation scripts for both API and UI testing using Python. The project covers:

- **API automation** using `pytest` for `reqres.in` with libraries `requests` and `assertpy`
- **UI automation** using `selenium` framework for `saucedemo.com`
  
# Libraries Used
requests - For making HTTP requests in Python.
assertpy - For assertions in tests.
selenium - For browser automation.
pytest - For running the tests.
allure-pytest - For generating test reports.

# How to run test for this project
1. run pytest using this command = pytest -v --alluredir=build/allure-results
2. after run pytest, we have to generate the allure report using this command = allure generate build/allure-results --clean -o build/allure-report

   
