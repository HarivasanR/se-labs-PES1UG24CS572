# Lab 7 — Evidence to Capture

The handout requires a PDF containing genuine terminal screenshots. These cannot be generated accurately without running the program in your local Python environment.

Capture the following screenshots from this directory:

1. **Initial application run:** run the original buggy program from `before/shopping_cart.py` and show a normal sample execution.
2. **Failing fuzz tests:** temporarily run the test suite against the buggy implementation (keep a copy of the fixed `shopping_cart.py`, then place the baseline implementation at the import path as `shopping_cart.py`). Run `python -m pytest -q test_shopping_cart.py` and capture the Hypothesis failures.
3. **Fixed application run:** run `python shopping_cart.py` with valid sample inputs and capture the output.
4. **Passing fuzz tests:** run `python -m pytest -q test_shopping_cart.py` against the fixed implementation and capture the passing result.

Do not label fabricated or illustrative output as test evidence. Assemble the four genuine screenshots into one PDF for submission.
