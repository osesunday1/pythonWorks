toppings = ['mushrooms', 'green peppers', 'extra cheese', 'pepperoni']
for topping in toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    elif topping == 'pepperoni':               # ← new block
        print("Adding pepperoni (fan favorite)!")
    else:
        print(f"Adding {topping}.")
print("Finished making your pizza!")
