from hypothesis import given, strategies as st

from shopping_cart import cart_total, delivery_zone, promo_percent


@given(st.text() | st.none())
def test_cart_total_no_crash(value):
    result = cart_total(value)
    assert isinstance(result, int)
    assert result >= 0


@given(st.text() | st.none())
def test_promo_percent_no_crash(value):
    result = promo_percent(value)
    assert isinstance(result, int)
    assert 0 <= result <= 100


@given(st.text() | st.none())
def test_delivery_zone_no_crash(value):
    assert delivery_zone(value) in {"North", "West", "South", "East", "Unknown"}


@given(
    st.lists(
        st.tuples(
            st.text(alphabet=st.characters(whitelist_categories=("Ll", "Lu")), min_size=1, max_size=12),
            st.integers(min_value=0, max_value=100000),
            st.integers(min_value=1, max_value=100),
        ),
        min_size=1,
        max_size=10,
    )
)
def test_cart_total_matches_sum(items):
    cart = ",".join(f"{name}:{price}x{quantity}" for name, price, quantity in items)
    assert cart_total(cart) == sum(price * quantity for _, price, quantity in items)


@given(st.integers(min_value=0, max_value=100))
def test_promo_percent_valid_codes(percentage):
    assert promo_percent(f"OFF{percentage}") == percentage


@given(
    st.sampled_from(list("12345678")),
    st.text(alphabet="0123456789", min_size=5, max_size=5),
)
def test_delivery_zone_valid_pincodes(first_digit, remaining_digits):
    expected = {
        "1": "North", "2": "North", "3": "West", "4": "West",
        "5": "South", "6": "South", "7": "East", "8": "East",
    }
    assert delivery_zone(first_digit + remaining_digits) == expected[first_digit]
