# q4.py — Gradebook
# What this program does (beginner-friendly):
# 1) Ask how many students.
# 2) For each student: ask their name and a comma-separated list of scores (e.g., 78, 95, 88).
# 3) Clean + convert scores to integers; warn and skip any bad/empty pieces.
# 4) Print each student's average.
# 5) Print the class average (average of the student averages).
#
# Key ideas:
# - List of dictionaries: [{"name": "Ada", "scores": [78,95,88]}, ...]
# - Helper functions: parse_int_list (clean/convert), average (safe average)

def parse_int_list(csv_text: str) -> list[int]:
    """
    Convert text like '78, 95, x, 88,  ' into [78, 95, 88].
    - Split on commas
    - Strip spaces
    - Try to int() each piece
    - Warn and skip invalid or empty pieces
    """
    out: list[int] = []
    for raw in csv_text.split(","):
        piece = raw.strip()
        if not piece:  # empty chunk (e.g., trailing comma)
            print("Skipping empty score.")
            continue
        try:
            out.append(int(piece))
        except ValueError:
            print(f"Skipping invalid score '{piece}'.")
    return out

def average(nums: list[int]) -> float:
    """Return the arithmetic mean of nums; return 0.0 if the list is empty."""
    return (sum(nums) / len(nums)) if nums else 0.0

def ask_positive_int(prompt: str) -> int:
    """Ask until the user types a whole number ≥ 0; return it as int."""
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if n < 0:
                print("Please enter 0 or a positive whole number.")
                continue
            return n
        except ValueError:
            print("Please enter a whole number (e.g., 2).")

def ask_nonempty(prompt: str) -> str:
    """Ask until a non-empty string is entered; return it."""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Value cannot be empty.")

def main():
    print("=== GRADEBOOK SETUP ===")
    num_students = ask_positive_int("How many students? ")

    # Collect students
    students: list[dict] = []
    for i in range(1, num_students + 1):
        name = ask_nonempty(f"Student {i} name: ")
        scores_text = input(f"Enter scores for {name} (comma-separated): ")
        scores = parse_int_list(scores_text)
        students.append({"name": name, "scores": scores})

    # Compute and print per-student averages
    print("\n--- STUDENT AVERAGES ---")
    per_student_avgs: list[float] = []
    for stu in students:
        stu_avg = average(stu["scores"])
        per_student_avgs.append(stu_avg)
        # Format to 2 decimals; handle empty-score case gracefully (avg = 0.00)
        print(f"{stu['name']}: {stu_avg:.2f}")

    # Class average = average of student averages
    class_avg = average(per_student_avgs)
    print("\n--- CLASS AVERAGE ---")
    print(f"{class_avg:.2f}")

if __name__ == "__main__":
    main()
