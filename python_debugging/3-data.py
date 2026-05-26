#!/usr/bin/env python3
"""
Lab: Following the data.

Goal: compute total order amount after discount.
The script runs but produces wrong totals due to bad data propagation
across multiple functions.
"""


def parse_discount_rate(percent_text):
    """Convert percentage text to decimal rate (e.g. '10' -> 0.10)."""
    value = float(percent_text)
    return value


def compute_subtotal(items):
    """Return subtotal from (name, price, qty) rows."""
    subtotal = 0.0
    # _ is a convention to indicate unused/unwanted unpacked data
    for _, unit_price, qty in items:
        # print(f"Processing item {_}, amount {qty}, unit price {unit_price}")
        subtotal += unit_price * qty
        # print(f"  Added {_}(s) to pre-discount total (now {subtotal})")
    return subtotal


def apply_discount(subtotal, discount_rate):
    """Apply percentage discount to subtotal."""
    # Logic error: rate is given as "percentage amount"
    # Needs to divide by 100.
    # return subtotal * (1 - discount_rate)
    return subtotal * (1 - discount_rate/100)


def compute_final_total(items, discount_text):
    """Compute final total from cart rows and textual discount."""
    # Gets the total by summing each item amount multiplied by items amount
    subtotal = compute_subtotal(items)
    # Converts the input rate into actual number manipulable with maths.
    rate = parse_discount_rate(discount_text)
    # print(f"Got appliable rate: {rate}")
    discounted_amount = apply_discount(subtotal, rate)
    return round(discounted_amount, 2)


def main():
    cart = [
        ("notebook", 12.50, 2),
        ("pen", 1.20, 5),
        ("eraser", 0.80, 1),
    ]
    discount_text = "10"
    final_total = compute_final_total(cart, discount_text)
    print("Final total:", final_total)


if __name__ == "__main__":
    main()
