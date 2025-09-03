# Part A: Checking for special items in a list

# 1) Make a list of toppings (data to work with)
toppings = ['mushrooms', 'green peppers', 'extra cheese']

# 2) Loop through each topping in the list
for topping in toppings:
    # 3) If the topping is 'green peppers', print a special message
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    # 4) Otherwise, print that we are adding the topping
    else:
        print(f"Adding {topping}.")

# 5) After the loop finishes, print a final message
print("Finished making your pizza!")
