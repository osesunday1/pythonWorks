# Part B: Checking for empty lists

# Test 1: empty list
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")

print("---")

# Test 2: non-empty list
requested_toppings = ['pepperoni', 'mushrooms']

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")
