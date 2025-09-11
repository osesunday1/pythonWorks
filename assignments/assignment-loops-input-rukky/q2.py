"""
Q2 — City Collector

Ask the user to type city names one by one.
Stop when the user types 'done'.
Finally, show the list of all the cities entered.
"""

def main():
    print("=== City Collector ===")
    cities = []

    while True:
        city = input("Enter a city name (or 'done' to finish): ").strip()
        if city.lower() == "done":
            break
        if city == "":
            print("You typed nothing. Try again.")
            continue
        cities.append(city)

    print("\nYou entered these cities:")
    for c in cities:
        print("-", c)


if __name__ == "__main__":
    main()
