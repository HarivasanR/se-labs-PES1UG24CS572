"""Statement-coverage tests for shopping_cart.py."""
import pytest

from shopping_cart import cart_discount, item_total, shipping_fee


@pytest.mark.parametrize(
    ("category", "price", "qty", "expected"),
    [
        ("food", 100, 2, 210),
        ("electronics", 100, 1, 118),
        ("clothing", 100, 1, 112),
        ("food", 100, 10, 945),
    ],
)
def test_item_total_valid_categories_and_bulk_discount(category, price, qty, expected):
    assert item_total(category, price, qty) == expected


@pytest.mark.parametrize(
    ("category", "price", "qty", "message"),
    [
        ("toys", 100, 1, "unknown category"),
        ("food", -1, 1, "invalid price or quantity"),
        ("food", 100, 0, "invalid price or quantity"),
    ],
)
def test_item_total_validation(category, price, qty, message):
    with pytest.raises(ValueError, match=message):
        item_total(category, price, qty)


@pytest.mark.parametrize(
    ("cart_value", "is_prime", "coupon", "expected"),
    [
        (6000, False, "", 500),
        (3000, False, "", 200),
        (500, False, "", 0),
        (500, True, "", 100),
        (1500, False, "FLAT10", 150),
        (900, False, "FLAT10", 0),
    ],
)
def test_cart_discount_scenarios(cart_value, is_prime, coupon, expected):
    assert cart_discount(cart_value, is_prime, coupon) == expected


@pytest.mark.parametrize(
    ("cart_value", "is_prime", "is_express", "expected"),
    [
        (1000, False, False, 0),
        (100, False, False, 40),
        (100, False, True, 140),
        (100, True, False, 0),
        (100, True, True, 50),
    ],
)
def test_shipping_fee_scenarios(cart_value, is_prime, is_express, expected):
    assert shipping_fee(cart_value, is_prime, is_express) == expected
