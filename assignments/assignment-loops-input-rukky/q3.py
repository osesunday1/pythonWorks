"""
Q3 — Simple Shop Bill

Enter items (name, price, quantity). Type 'done' as the item name to finish.
Print a simple receipt showing each item's line total and the grand total.
"""

def get_positive_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0:
                print("Please enter a non-negative number.")
                continue
            return v
        except ValueError:
            print("That's not a number. Try again (use digits like 3.50).")

def get_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v <= 0:
                print("Please enter a whole number greater than 0.")
                continue
            return v
        except ValueError:
            print("That's not a whole number. Try again (use digits like 1, 2).")

def main():
    print("=== Simple Shop Bill ===")
    items = []  # list of (name, unit_price, qty, line_total)

    while True:
        name = input("Enter item name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if name == "":
            print("You typed nothing. Try again.")
            continue

        price = get_positive_float(f"Enter unit price for '{name}': ")
        qty = get_positive_int(f"Enter quantity for '{name}': ")

        line_total = price * qty
        items.append((name, price, qty, line_total))
        print(f"Added: {qty} x {name} at {price} each -> line total {line_total:.2f}\n")

    print("\n=== Receipt ===")
    if not items:
        print("No items were entered.")
        return

    subtotal = 0.0
    for name, price, qty, line_total in items:
        print(f"{qty} x {name} @ {price:.2f} = {line_total:.2f}")
        subtotal += line_total

    print(f"\nSubtotal: {subtotal:.2f}")
    # Optional simple tax example (commented out). If you want tax, set TAX_RATE and uncomment:
    # TAX_RATE = 0.06
    # tax = subtotal * TAX_RATE
    # print(f"Tax ({TAX_RATE*100:.0f}%): {tax:.2f}")
    # print(f"Total: {subtotal + tax:.2f}")

    print(f"Total: {subtotal:.2f}")

if __name__ == "__main__":
    main()
