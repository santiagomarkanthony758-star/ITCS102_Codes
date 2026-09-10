# Code Challenge3

sender_name = "Anthony"

item_type = input("Enter type of item: ")
is_fragile = input("Is the item fragile? (True/False): ") == "True"

weight = float(input("Enter weight in kg: "))
distance = float(input("Enter distance in km: "))

is_express = input("Is it express? (True/False): ") == "True"
is_international = input("Is it international? (True/False): ") == "True"

# Calculate Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

# Pricing Tiers
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00
    rate = "Free Shipping"

elif is_international and is_express:
    total = (base_cost * 1.40) + 50
    rate = "International Express"

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25
    rate = "Express or Heavy International"

elif weight > 30 or distance > 1000:
    total = base_cost + 30
    rate = "Oversized"

else:
    total = base_cost
    rate = "Standard Rate"

# Display Results
print("\n--- SHIPPING DETAILS ---")
print(f"Sender Name: {sender_name}")
print(f"Type of Item: {item_type}")
print(f"Fragile: {is_fragile}")
print(f"Weight: {weight} kg")
print(f"Distance: {distance} km")
print(f"Express: {is_express}")
print(f"International: {is_international}")
print(f"Rate: {rate}")
print(f"Total Shipping Cost: ${total:.2f}")