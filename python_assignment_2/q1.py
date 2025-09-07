# q1.py — Squares & Evens
# 1) Ask for comma-separated integers
# 2) Clean + convert; warn/skip bad pieces
# 3) Print "n → n^2" for each valid number
# 4) Collect squares of even numbers; print list + length

def parse_integers(csv_text: str):
    numbers = []
    for raw in csv_text.split(","):
        piece = raw.strip()
        if not piece:
            print("Skipping empty entry.")
            continue
        try:
            n = int(piece)
            numbers.append(n)
        except ValueError:
            print(f"Skipping invalid entry '{piece}' — not an integer.")
    return numbers

def main():
    user_text = input("Enter integers separated by commas (e.g., 3, 6, 1, 4): ")
    nums = parse_integers(user_text)

    even_squares = []
    for n in nums:
        sq = n * n
        print(f"{n} \u2192 {sq}")
        if n % 2 == 0:
            even_squares.append(sq)

    print(f"\nEven squares: {even_squares}")
    print(f"Count: {len(even_squares)}")

if __name__ == "__main__":
    main()
