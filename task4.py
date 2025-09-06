# task4.py
# Approach:
# 1. Ask for number of students.
# 2. For each student, collect name and scores (validated, converted to integers).
# 3. Store as a dictionary in a list: {"name": "Ada", "scores": [78, 95, 88]}.
# 4. Compute and print each student’s average.
# 5. Compute class average (average of student averages).
# 6. Bonus: Print a summary table aligned in columns.

students = []

# Step 1: Get number of students
while True:
    try:
        n = int(input("Enter the number of students: "))
        if n <= 0:
            print("⚠️ Please enter a positive number.")
            continue
        break
    except ValueError:
        print("⚠️ Invalid input! Please enter a whole number.")

# Step 2: Collect student data
for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ").strip()
    raw_scores = input(f"Enter comma-separated scores for {name}: ")

    scores = []
    for part in raw_scores.split(","):
        part = part.strip()
        if part == "":
            continue
        try:
            scores.append(int(part))
        except ValueError:
            print(f"⚠️ Warning: '{part}' is not a valid score. Skipped.")

    if not scores:
        print(f"⚠️ No valid scores entered for {name}. Defaulting to [0].")
        scores = [0]

    students.append({"name": name, "scores": scores})

# Step 3 & 4: Compute averages
student_averages = []
for student in students:
    avg = sum(student["scores"]) / len(student["scores"])
    student_averages.append(avg)

# Step 5: Class average
class_avg = sum(student_averages) / len(student_averages)

# Step 6: Print results
print("\n📊 Gradebook Summary")
print("-" * 40)
print(f"{'Name':<15}{'Scores':<20}{'Average':>8}")
print("-" * 40)
for student, avg in zip(students, student_averages):
    scores_str = ", ".join(map(str, student["scores"]))
    print(f"{student['name']:<15}{scores_str:<20}{avg:>8.2f}")
print("-" * 40)
print(f"{'Class Average':<35}{class_avg:>8.2f}")
