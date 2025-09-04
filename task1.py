# task1.py
# Approach:
# 1. Ask user for a comma-separated list of integers.
# 2. Clean and validate inputs (skip invalid entries with a warning).
# 3. Print each number with its square using a for loop.
# 4. Build a new list of squares of even numbers.
# 5. Print the list and its length.

raw = input("Enter a comma-separated list of integers: ")

# Step 1: split input and clean whitespace
items = [x.strip() for x in raw.split(",")]

numbers = []

# Step 2: validate inputs
for item in items:
    try:
        numbers.append(int(item))
    except ValueError:
        print(f"Warning: '{item}' is not a valid integer and will be skipped.")

# Step 3 & 4: process numbers
even_squares = []
for n in numbers:
    print(f"{n} → {n**2}")
    if n % 2 == 0:
        even_squares.append(n**2)

# Step 5: final output
print(f"Even squares list: {even_squares}")
print(f"Length: {len(even_squares)}")
