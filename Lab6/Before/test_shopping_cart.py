import pytest
from shopping_cart import item_total, cart_discount, shipping_fee

# Original starter test cases (before coverage improvement).
def test_food_item():
    assert item_total("food", 100, 2) == 210

def test_free_shipping():
    assert shipping_fee(1000, False, False) == 0
