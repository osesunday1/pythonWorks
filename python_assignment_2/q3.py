
# q3.py — Simple Shop Bill (FULL VERSION)
# What this program does:
# 1) Build a product catalog (name → price).
# 2) Let you add purchases as "item,quantity" repeatedly.
# 3) Stop when you type checkout / check out / check-out / done / quit / exit.
# 4) Print an itemized bill and the grand total.
#
# Notes for beginners:
# - The "input loop" is just the WHILE TRUE block that keeps asking you for input.

def ask_positive_float(prompt):
    """Ask until the user provides a non-negative number; return it as float."""
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0:
                print("Please enter a non-negative number.")
                continue
            return v
        except ValueError:
            print("Invalid number. Try again (e.g., 2 or 2.5).")

def ask_nonempty(prompt):
    """Ask until a non-empty string is given; return the string."""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Value cannot be empty.")

def main():
    print("=== CATALOG SETUP ===")
    # How many items will you put in the catalog?
    while True:
        s = input("How many items in the catalog? ").strip()
        try:
            n = int(s)
            if n < 0:
                print("Enter 0 or a positive whole number.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (e.g., 3).")

    # Build the catalog: store by lowercase key so lookups are easy
    catalog = {}  # key: lowercased item name -> price (float)
    for i in range(1, n + 1):
        name = ask_nonempty(f"Item {i} name: ")
        price = ask_positive_float(f"Price for '{name}': ")
        catalog[name.lower()] = price

    print("\n=== SHOPPING ===")
    print("Enter purchases as 'item,quantity' (e.g., milk,3).")
    print("Type 'checkout' (or 'check out', 'done', 'quit', 'exit') to finish.")

    bill = []        # list of tuples: (display_name, qty (float), unit_price, line_total)
    grand_total = 0  # running sum

    # ---------- INPUT LOOP (keeps asking until you type a stop word) ----------
    while True:
        raw = input("> ").strip()

        if not raw:
            print("Empty input skipped.")
            continue

        # Normalize for stop words: remove spaces/dashes, lowercase
        normalized = raw.lower().replace(" ", "").replace("-", "")
        if normalized in {"checkout", "done", "finish", "pay", "quit", "exit"}:
            break

        # Expect "item,quantity"
        parts = [p.strip() for p in raw.split(",")]
        if len(parts) != 2:
            print("Format must be 'item,quantity' (e.g., apple,2).")
            continue

        item_name, qty_text = parts[0], parts[1]
        if not item_name:
            print("Item name cannot be empty.")
            continue

        key = item_name.lower()
        if key not in catalog:
            print(f"'{item_name}' is not in the catalog. Skipped.")
            continue

        # Quantity can be integer or decimal
        try:
            qty = float(qty_text)
            if qty <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Quantity must be a number (e.g., 2 or 1.5).")
            continue

        unit_price = catalog[key]
        line_total = unit_price * qty
        bill.append((item_name, qty, unit_price, line_total))
        grand_total += line_total
        print(f"Added: {item_name} × {qty} @ {unit_price:.2f} = {line_total:.2f}")
    # -------------------------------------------------------------------------

    # Print the results
    print("\n--- ITEMIZED BILL ---")
    if not bill:
        print("(no items)")
    else:
        for name, qty, unit, total in bill:
            print(f"{name:15} qty={qty:<6} unit={unit:<7.2f} line={total:>8.2f}")
        print("-" * 46)
        print(f"GRAND TOTAL: {grand_total:.2f}")

if __name__ == "__main__":
    main()
