
# Part E: Nested Dictionaries and Lists
# Idea: A dictionary of students; each student has a name, age, and a list of grades.

students = {
    's1': {'name': 'Bob', 'age': 17, 'grades': [85, 90, 78]},
    's2': {'name': 'Carol', 'age': 22, 'grades': [92, 88, 95]},
}

for sid, info in students.items():
    name = info['name']
    age = info['age']
    grades = info['grades']

    # Adult or not
    if age >= 18:
        print(f"{name} is an adult.")
    else:
        print(f"{name} is not an adult yet.")

    # Any grade below 80?
    if any(g < 80 for g in grades):
        print(f"Warning: {name} has a grade below 80.")

    # Summary report
    average = sum(grades) / len(grades)
    print(f"Summary for {name}: age={age}, grades={grades}, average={average:.1f}")
    print("---")
