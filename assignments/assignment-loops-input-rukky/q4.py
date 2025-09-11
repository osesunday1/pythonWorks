"""
Q4 — Gradebook

Enter student names and numeric grades (0-100). Type 'done' as the name to finish.
Print each student with a letter grade, plus class average, highest and lowest.
"""

def get_grade(prompt):
    while True:
        s = input(prompt).strip()
        try:
            g = int(s)
            if g < 0 or g > 100:
                print("Please enter a whole number between 0 and 100.")
                continue
            return g
        except ValueError:
            print("That's not a whole number. Try again (0-100).")

def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def main():
    print("=== Gradebook ===")
    records = []  # list of (name, grade)

    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if name == "":
            print("You typed nothing. Try again.")
            continue

        grade = get_grade(f"Enter numeric grade for '{name}' (0-100): ")
        records.append((name, grade))
        print(f"Recorded: {name} -> {grade}\n")

    print("\n=== Class Grades ===")
    if not records:
        print("No students were entered.")
        return

    total = 0
    highest = records[0]
    lowest = records[0]

    for name, grade in records:
        lg = letter_grade(grade)
        print(f"{name}: {grade} -> {lg}")
        total += grade
        if grade > highest[1]:
            highest = (name, grade)
        if grade < lowest[1]:
            lowest = (name, grade)

    count = len(records)
    avg = total / count
    print(f"\nStudents: {count}")
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest[0]} -> {highest[1]}")
    print(f"Lowest: {lowest[0]} -> {lowest[1]}")

if __name__ == "__main__":
    main()
