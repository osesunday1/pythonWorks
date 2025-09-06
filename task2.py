# task2.py
# Approach:
# 1. Continuously prompt user for city names using a while loop.
# 2. Stop when the user types 'done' (case-insensitive).
# 3. Store unique cities in a set to avoid duplicates.
# 4. Print number of unique cities and list them alphabetically with numbering.

cities = set()

while True:
    city = input("Enter a city you have visited (or type 'done' to finish): ").strip()
    if city.lower() == "done":
        break
    elif city == "":
        print("⚠️ Empty input ignored. Please enter a valid city.")
    else:
        cities.add(city)

sorted_cities = sorted(cities)

print(f"\nYou have visited {len(sorted_cities)} unique cities.")
for i, city in enumerate(sorted_cities, start=1):
    print(f"{i}. {city}")

