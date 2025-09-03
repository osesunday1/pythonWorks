
# Part D: Using a dictionary with if statements

# 1) One student record (dictionary = labeled facts)
student = {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}

# 2) Adult check
if student['age'] >= 18:
    print(f"{student['name']} is an adult.")
else:
    print(f"{student['name']} is not yet an adult.")

# 3) GPA rating (change the number to test)
student['GPA'] = 3.4

gpa = student['GPA']
if gpa >= 3.5:
    print("Excellent")
elif gpa >= 3.0:
    print("Good")
else:
    print("Needs Improvement")
