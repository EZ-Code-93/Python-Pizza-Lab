small_pizza = 8
large_pizza = 12
toppings = 1

# delivery fee
five_miles = 2
additional_miles = 1

print("\n\t--- Welcome to Python Pizza! ---")
size = input("\nEnter the size of the pizza (small/large): ")
extra_toppings = int(input("Enter the number of extra toppings: "))
distance = int(input("Enter the delivery distance in miles: "))

# calculate total cost
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

print(f"\nA {size} pizza with {extra_toppings} extra toppings and\n"
      f"a delivery distance of {distance} miles costs: ${total}\n")
