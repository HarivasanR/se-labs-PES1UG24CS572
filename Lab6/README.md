# Lab 6 — Code and Branch Coverage

**SRN:** PES1UG24CS572

This folder contains the supplied `shopping_cart.py` application and two independent pytest suites, as required by the Lab 6 handout.

## Install dependencies

```bash
python -m pip install pytest coverage
```

## Stage 1 — Statement/code coverage

Run from this folder:

```bash
coverage erase
coverage run -m pytest -q CodeCoverageTest_pes1ug24cs572_application.py
coverage report -m shopping_cart.py
```

The terminal output report is included as `code_coverage_report.svg`.

## Stage 2 — Branch coverage

```bash
coverage erase
coverage run --branch -m pytest -q BranchCoverageTest_pes1ug24cs572_application.py
coverage report -m shopping_cart.py
```

The terminal output report is included as `branch_coverage_report.svg`.

The application logic is kept unchanged from the supplied starter project. The two test suites are separate so each coverage stage can be run and documented independently.
