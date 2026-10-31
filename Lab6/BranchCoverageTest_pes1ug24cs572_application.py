"""Decision/branch-coverage tests for shopping_cart.py."""
import pytest

from shopping_cart import cart_discount, item_total, shipping_fee


@pytest.mark.parametrize(
    ("category", "price", "qty", "expected"),
    [
        ("food", 100, 1, 105),       # known category; no bulk discount
        ("electronics", 100, 10, 1062),  # bulk discount
        ("clothing", 100, 2, 224),
    ],
)
def test_item_total_success_branches(category, price, qty, expected):
    assert item_total(category, price, qty) == expected


@pytest.mark.parametrize(
    ("category", "price", "qty", "message"),
    [
        ("unknown", 100, 1, "unknown category"),
        ("food", -1, 1, "invalid price or quantity"),
        ("food", 100, 0, "invalid price or quantity"),
    ],
)
def test_item_total_error_branches(category, price, qty, message):
    with pytest.raises(ValueError, match=message):
        item_total(category, price, qty)


@pytest.mark.parametrize(
    ("cart_value", "is_prime", "coupon", "expected"),
    [
        (5000, False, "", 500),       # top tier
        (2000, False, "", 200),       # middle tier
        (1999, False, "", 0),         # lower tier
        (5000, True, "", 600),        # prime true
        (1000, False, "FLAT10", 100), # coupon and threshold true
        (999, False, "FLAT10", 0),    # coupon matches, threshold false
        (1500, False, "OTHER", 0),    # coupon comparison false
    ],
)
def test_cart_discount_decision_branches(cart_value, is_prime, coupon, expected):
    assert cart_discount(cart_value, is_prime, coupon) == expected


@pytest.mark.parametrize(
    ("cart_value", "is_prime", "is_express", "expected"),
    [
        (100, True, False, 0),     # prime base fee
        (100, False, False, 40),   # non-prime, below free-shipping threshold
        (500, False, False, 0),    # non-prime, threshold reached
        (100, False, True, 140),   # express for non-prime
        (100, True, True, 50),     # express for prime
    ],
)
def test_shipping_fee_decision_branches(cart_value, is_prime, is_express, expected):
    assert shipping_fee(cart_value, is_prime, is_express) == expected
