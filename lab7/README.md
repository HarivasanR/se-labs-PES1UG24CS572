# Lab 7 — Fuzz Testing with Hypothesis

## Objective
Use Hypothesis property-based testing to discover edge-case input failures in the three shopping-cart functions, then harden the application.

## Files
- `shopping_cart.py`: fixed application implementation.
- `test_shopping_cart.py`: Hypothesis fuzz tests and valid-input properties.
- `before/shopping_cart.py`: original buggy implementation supplied with the shopping-cart starter project.
- `EVIDENCE.md`: commands and checklist for the required screenshots/PDF.

## Setup
Run from this directory:

```bash
python -m pip install hypothesis pytest
```

## Run the fixed application
```bash
python shopping_cart.py
```
Example inputs: `pen:10x2,book:250x1`, `OFF20`, and `560085`.

## Run the tests
```bash
python -m pytest -q test_shopping_cart.py
```

## Validation behaviour
- `cart_total`: accepts comma-separated `name:pricexquantity` entries. Invalid or empty input, non-string input, malformed entries, and non-positive quantities return 0.
- `promo_percent`: accepts `OFF` followed by a percentage from 0 through 100, case-insensitively. Invalid values return 0.
- `delivery_zone`: accepts exactly six ASCII numeric digits. Invalid pincodes and unsupported first digits return `Unknown`.

Hypothesis generates arbitrary Unicode strings and `None` values, then checks valid generated carts, promo codes, and pincodes.
