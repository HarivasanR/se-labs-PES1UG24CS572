# Lab 6 — Code and Branch Coverage

**SRN:** PES1UG24CS572

This folder contains the supplied `shopping_cart.py` application, the original baseline test case, and the two expanded test suites required by the Lab 6 handout.

## Before: original starter tests

The original starter file is in `Before/test_shopping_cart.py`. It contains the two supplied tests and is used as the baseline for both coverage measurements.

Run these commands from the `Lab6` folder:

```bash
coverage erase
coverage run -m pytest -q Before/test_shopping_cart.py
coverage report -m shopping_cart.py
```

Baseline statement/code coverage: **44%**.

```bash
coverage erase
coverage run --branch -m pytest -q Before/test_shopping_cart.py
coverage report -m shopping_cart.py
```

Baseline branch coverage: **37%**.

## After: expanded code coverage tests

Install dependencies:

```bash
python -m pip install pytest coverage
```

Run:

```bash
coverage erase
coverage run -m pytest -q CodeCoverageTest_pes1ug24cs572_application.py
coverage report -m shopping_cart.py
```

Result: **100% statement/code coverage**.

Terminal output: [code_coverage_terminal.svg](code_coverage_terminal.svg)

## After: expanded branch coverage tests

Run:

```bash
coverage erase
coverage run --branch -m pytest -q BranchCoverageTest_pes1ug24cs572_application.py
coverage report -m shopping_cart.py
```

Result: **100% branch coverage**.

Terminal output: [branch_coverage_terminal.svg](branch_coverage_terminal.svg)

## Before/after comparison

| Measurement | Before | After |
|---|---:|---:|
| Statement/code coverage | 44% | 100% |
| Branch coverage | 37% | 100% |

The application logic in `shopping_cart.py` is unchanged. The improvement comes from adding tests that exercise the previously uncovered statements and decision branches.
