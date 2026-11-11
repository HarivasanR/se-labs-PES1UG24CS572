import re

ZONES = {
    "1": "North", "2": "North", "3": "West", "4": "West",
    "5": "South", "6": "South", "7": "East", "8": "East",
}


def cart_total(cart):
    """Return the total for a cart; malformed input safely returns 0."""
    if not isinstance(cart, str) or not cart.strip():
        return 0

    total = 0
    try:
        for item in cart.split(","):
            if ":" not in item:
                return 0
            name, rest = item.split(":", 1)
            if not name.strip():
                return 0
            match = re.fullmatch(r"\s*(\d+)\s*[xX]\s*(\d+)\s*", rest)
            if not match:
                return 0
            price, quantity = map(int, match.groups())
            if quantity <= 0:
                return 0
            total += price * quantity
    except (TypeError, ValueError, OverflowError):
        return 0
    return total


def promo_percent(code):
    """Return a valid OFF percentage from 0 to 100; invalid input returns 0."""
    if not isinstance(code, str):
        return 0
    match = re.fullmatch(r"\s*OFF(\d{1,3})\s*", code, flags=re.IGNORECASE)
    if not match:
        return 0
    percentage = int(match.group(1))
    return percentage if 0 <= percentage <= 100 else 0


def delivery_zone(pincode):
    """Return the zone for a six-digit numeric pincode, otherwise Unknown."""
    if not isinstance(pincode, str) or not re.fullmatch(r"\d{6}", pincode):
        return "Unknown"
    return ZONES.get(pincode[0], "Unknown")


def main():
    print("==== Running cart_total ====")
    cart = input("Enter cart as name:pricexqty CSV (e.g. pen:10x2,book:250x1): ")
    print("Cart Total:", cart_total(cart))

    print("\n==== Running promo_percent ====")
    code = input("Enter a promo code (e.g. OFF20): ")
    print("Discount Percent:", promo_percent(code))

    print("\n==== Running delivery_zone ====")
    pincode = input("Enter a 6 digit pincode (e.g. 560085): ")
    print("Delivery Zone:", delivery_zone(pincode))


if __name__ == "__main__":
    main()
