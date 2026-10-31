# Lab 6 — Code and Branch Coverage

**SRN:** PES1UG24CS572

This folder contains the supplied `shopping_cart.py` application and the two independent test suites required by the Lab 6 handout.

## Install dependencies

```bash
python -m pip install pytest coverage
```

## Code coverage

Run from this folder:

```bash
coverage erase
coverage run -m pytest -q CodeCoverageTest_pes1ug24cs572_application.py
coverage report -m shopping_cart.py
```

Terminal output: [code_coverage_terminal.svg](code_coverage_terminal.svg)

## Branch coverage

```bash
coverage erase
coverage run --branch -m pytest -q BranchCoverageTest_pes1ug24cs572_application.py
coverage report -m shopping_cart.py
```

Terminal output: [branch_coverage_terminal.svg](branch_coverage_terminal.svg)

The application logic is unchanged from the supplied starter project. Each coverage stage has its own test suite and terminal-output capture.
