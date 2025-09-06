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
# task3.py
# Approach:
# 1. Catalog setup: user enters items and prices (stored in dictionary).
# 2. Shopping phase: user enters purchases as item,quantity until 'checkout'.
# 3. Compute itemized bill and grand total.
# 4. Allow user to enter a discount code (e.g., SAVE10, SAVE20).
# 5. Apply discount if valid, then print final total.

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
        print("⚠️ Invalid input! Please enter a whole number.")

for i in range(n):
    name = input(f"Enter name for item {i+1}: ").strip().lower()
    while True:
        try:
            price = float(input(f"Enter price for '{name}': "))
            if price < 0:
                print("⚠️ Price cannot be negative.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid price! Please enter a number.")
    catalog[name] = price

print("\nCatalog setup complete ✅")
print("Available items:", catalog)

# Phase 2: Shopping
cart = []
while True:
    entry = input("\nEnter item and quantity (item,quantity) or 'checkout' to finish: ").strip().lower()
    if entry == "checkout":
        break

    if "," not in entry:
        print("⚠️ Invalid format. Use item,quantity (e.g., milk,3).")
        continue

    item, qty = entry.split(",", 1)
    item, qty = item.strip(), qty.strip()

    if not qty.isdigit():
        print(f"⚠️ Quantity '{qty}' is not valid. Skipping...")
        continue
    qty = int(qty)

    if item not in catalog:
        print(f"⚠️ Item '{item}' not found in catalog. Skipping...")
        continue

    line_total = catalog[item] * qty
    cart.append((item, qty, line_total))
    print(f"Added {qty} x {item} → ${line_total:.2f}")

# Compute totals
grand_total = sum(line[2] for line in cart)

# Phase 3: Discount
discount_codes = {"SAVE10": 0.10, "SAVE20": 0.20}
discount_applied = 0

code = input("\nDo you have a discount code? (Enter or press Enter to skip): ").strip().upper()
if code:
    if code in discount_codes:
        discount_applied = discount_codes[code]
        print(f"✅ Discount code '{code}' applied ({int(discount_applied*100)}% off).")
    else:
        print(f"⚠️ Code '{code}' is invalid. No discount applied.")

final_total = grand_total * (1 - discount_applied)

# Phase 4: Print bill
print("\n🧾 Itemized Bill")
print("-" * 40)
print(f"{'Item':<12}{'Qty':<5}{'Price':<8}{'Total':>8}")
print("-" * 40)
for i, (item, qty, line_total) in enumerate(cart, start=1):
    print(f"{item:<12}{qty:<5}{catalog[item]:<8.2f}{line_total:>8.2f}")
print("-" * 40)
print(f"{'Original Total':<27}${grand_total:>8.2f}")
if discount_applied > 0:
    print(f"{'Discount Applied':<27}- {int(discount_applied*100)}%")
print(f"{'Final Total':<27}${final_total:>8.2f}")

