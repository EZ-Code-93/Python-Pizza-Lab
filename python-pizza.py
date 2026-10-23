# Cost variables for pizza and delivery
small_pizza = 8
large_pizza = 12
toppings = 1

# delivery fee
five_miles = 2
additional_miles = 1
# Welcome message for the user
print("\n\t--- Welcome to Python Pizza! ---")

# while loop with input validation to get valid pizza size from the user
while True:
    size = input("\nEnter the size of the pizza (small/large): ").strip().lower()
    if size in ["small", "large"]:
        break
    print("Invalid choice. Please enter exactly 'small' or 'large'.")

# while loop with input validation to get valid number of extra toppings from the user
while True:
    try:
        extra_toppings = int(input("Enter the number of extra toppings: "))
        if extra_toppings >= 0:
            break
        print("Toppings cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# while loop with input validation to get valid delivery distance from the user
while True:
    try:
        distance = int(input("Enter the delivery distance in miles: "))
        if distance >= 0:
            break
        print("Distance cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# take in the user's choices and calculate the total cost
total = 0
if size == "small":
    total += small_pizza
elif size == "large":
    total += large_pizza

total += extra_toppings * toppings

if distance <= 5:
    total += five_miles
else:
    total += five_miles + (distance - 5) * additional_miles

# print the final order summary and total cost to the user
print(f"\nA {size} pizza with {extra_toppings} extra toppings and\n"
      f"a delivery distance of {distance} miles costs: ${total}\n")
