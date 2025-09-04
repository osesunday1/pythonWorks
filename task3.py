# task3.py
# Approach:
# 1. Phase 1: Ask the user how many items to add to the catalog.
#    - For each item, prompt for name and price (validated as float).
#    - Store in a dictionary {name: price}.
# 2. Phase 2: Ask the user repeatedly for "item,quantity" until 'checkout'.
#    - Validate input format and quantities.
#    - If item not in catalog, print a warning and skip.
#    - Keep track of purchases and compute totals.
# 3. Print itemized bill and grand total at the end.

catalog = {}

# Phase 1: Catalog setup
while True:
    try:
        n = int(input("How many items to add to the catalog? "))
        if n <= 0:
            print("⚠️ Please enter a positive number.")
            continue
        break
    except ValueError:
        print("⚠️ Invalid input! Enter a whole number.")

for i in range(n):
    name = input(f"Enter name for item {i+1}: ").strip()
    while True:
        try:
            price = float(input(f"Enter price for '{name}': "))
            if price <= 0:
                print("⚠️ Price must be greater than zero.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid price! Enter a number (e.g., 2.5).")
    catalog[name] = price

print("\nCatalog setup complete ✅")
print("Available items:", catalog)

# Phase 2: Shopping
cart = []
while True:
    entry = input("\nEnter item and quantity (item,quantity) or 'checkout' to finish: ").strip()
    if entry.lower() == "checkout":
        break

    if "," not in entry:
        print("⚠️ Please use the format item,quantity (e.g., milk,3).")
        continue

    item, qty = entry.split(",", 1)
    item = item.strip()
    qty = qty.strip()

    # Validate quantity
    try:
        qty = int(qty)
        if qty <= 0:
            print("⚠️ Quantity must be a positive number.")
            continue
    except ValueError:
        print("⚠️ Invalid quantity! Please enter a whole number.")
        continue

    # Check if item exists
    if item not in catalog:
        print(f"⚠️ Item '{item}' not found in catalog. Skipping...")
        continue

    # Add to cart
    line_total = catalog[item] * qty
    cart.append((item, qty, catalog[item], line_total))
    print(f"Added {qty} x {item} → ${line_total:.2f}")

# Final Bill
print("\n🧾 Itemized Bill")
print("-" * 30)
grand_total = 0
for i, (item, qty, price, total) in enumerate(cart, start=1):
    print(f"{i}. {item} ({qty} @ ${price:.2f}) = ${total:.2f}")
    grand_total += total

print("-" * 30)
print(f"Grand Total: ${grand_total:.2f}")
