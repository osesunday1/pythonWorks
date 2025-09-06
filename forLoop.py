#The for loop is used to repeat a block of code for each item in a sequence (like a list, tuple, string, or range).
'''
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for i in range(5):
    print(i)

'''

prices = [20, 15, 30, 10]  # prices of items
total = 0

for price in prices:
   total=total+price
   #total += price

print("Total shopping cost =", total)