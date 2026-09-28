from decimal import Decimal

def calculate_estimated_value(weight_kg, price_per_kg):
    weight = Decimal(str(weight_kg))
    price = Decimal(str(price_per_kg))
    if weight < 0 or price < 0:
        raise ValueError("Weight and price cannot be negative.")
    return weight * price
