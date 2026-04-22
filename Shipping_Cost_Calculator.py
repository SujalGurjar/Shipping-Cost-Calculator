def calculate_shipping_cost(weight, distance):
    rate_per_kg = 5
    rate_per_km = 0.1
    cost = (weight * rate_per_kg) + (distance * rate_per_km)
    return cost

weight = float(input("Enter weight (kg): "))
distance = float(input("Enter distance (km): "))
print(f"Shipping Cost: ${calculate_shipping_cost(weight, distance):.2f}")
