"""
Q1 — Squares & Evens

Ask the user for a positive integer N,
then print i^2 for i from 1 to N and say if the square is even or odd.
"""
def get_positive_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if n <= 0:
                print("Please type a positive whole number like 1, 2, 3...")
                continue
            return n
        except ValueError:
            print("That's not a whole number. Try again with digits like 4 or 10.")

def main():
    print("=== Squares & Evens ===")
    n = get_positive_int("Enter a positive integer N: ")
    print(f"\nSquares from 1 to {n}:")
    for i in range(1, n + 1):
        sq = i * i
        kind = "even" if sq % 2 == 0 else "odd"
        print(f"{i}^2 = {sq} -> {kind}")

if __name__ == "__main__":
    main()
