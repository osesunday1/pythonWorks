# Test with empty list
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")

print("\n---\n")

# Test with non-empty list
requested_toppings = ['pepperoni', 'olives', 'cheese']

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")
