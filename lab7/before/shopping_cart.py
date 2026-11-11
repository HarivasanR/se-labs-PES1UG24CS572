ZONES = {"1": "North", "2": "North", "3": "West", "4": "West",
         "5": "South", "6": "South", "7": "East", "8": "East"}


def cart_total(cart):
    total = 0
    for item in cart.split(','):
        name, rest = item.split(':')
        price, qty = rest.split('x')
        total += int(price) * int(qty)
    return total


def promo_percent(code):
    return int(code.upper().split('OFF')[1])


def delivery_zone(pincode):
    return ZONES[pincode[0]]


def main():
    print("==== Running cart_total ====")
    user_input = input("Enter cart as name:pricexqty CSV (e.g. pen:10x2,book:250x1): ")
    print("Cart Total:", cart_total(user_input))

    print("\n==== Running promo_percent ====")
    user_input = input("Enter a promo code (e.g. OFF20): ")
    print("Discount Percent:", promo_percent(user_input))

    print("\n==== Running delivery_zone ====")
    user_input = input("Enter a 6 digit pincode (e.g. 560085): ")
    print("Delivery Zone:", delivery_zone(user_input))


if __name__ == "__main__":
    main()
