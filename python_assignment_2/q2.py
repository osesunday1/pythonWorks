# q2.py — City Collector
# Repeatedly ask for city names until user types 'done'/'quit'/'exit'.
# Ignore empty inputs. Keep each city only once (case-insensitive).
# Finally, print the unique cities sorted alphabetically and the total count.

SENTINELS = {"done", "quit", "exit"}

def main():
    seen_lower = set()      # track uniques using lowercase
    unique_cities = []      # keep original casing for display

    while True:
        raw = input("Enter a city (type 'done' to finish): ").strip()
        if not raw:
            print("Empty input skipped.")
            continue
        if raw.lower() in SENTINELS:
            break

        key = raw.lower()
        if key in seen_lower:
            print(f"'{raw}' already added — duplicate ignored.")
            continue

        seen_lower.add(key)
        unique_cities.append(raw)

    unique_sorted = sorted(unique_cities, key=str.lower)

    print("\nUnique cities (sorted):")
    for i, city in enumerate(unique_sorted, start=1):
        print(f"{i}. {city}")
    print(f"\nTotal unique cities: {len(unique_sorted)}")

if __name__ == "__main__":
    main()
