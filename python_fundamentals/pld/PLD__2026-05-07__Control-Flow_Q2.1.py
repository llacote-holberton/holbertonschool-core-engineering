#!/usr/bin/env python3
# PLD Exercises answered and explained

# === PYTHON - ENVIRONMENT & FIRST PROGRAMS ===

# === PYTHON - CONTROL FLOW ===



# Let's piggyback on the payment process example.
# First define statically an example user
# We use the "dict" type because it's a mutable sequence
testUser_Laurent = {
    "id": 1,
    "name": "Laurent",
    "password": "s425Sheeuirojsdzhiuh3284",
    "payment_methods":
    {
        "card": "4444555566667777",
        "paypal": "laurent@testpaypal.com"
    }
}

testUser_Bob = {
    "id": 2,
    "name": "Bob",
    "password": "s425Sheeuirojsdzhiuh3284",
    "payment_methods": {}
}

# We want to check any payment method is defined
# To not try payment for nothing (typically we use a third-party API which costs us a penny every request)
def check_user_can_pay(user):
# First we define the "positive condition" = user has any payment method
# (user.payment_methods.card or user.payment_methods.paypal)
# Then we just "negate" it to trigger a message if none present.
    payment_methods = user.get("payment_methods")
    if not(payment_methods.get("card") or payment_methods.get("paypal")):
        print(f"Sorry {user['name']} no payment method registered for your account, please add one to proceed")
        return False
    else:
        print(f"{user['name']}, you have {len(payment_methods)} payment method registered please select one in the next step.")
        return True

check_user_can_pay(testUser_Laurent)
check_user_can_pay(testUser_Bob)
