
# Part F: Combining dictionaries in a list

books = [
    {'title': 'Python Basics', 'author': 'John Doe', 'copies': 3},
    {'title': 'AI with Python', 'author': 'Jane Smith', 'copies': 0},
    {'title': 'Data Science 101', 'author': 'Emily Davis', 'copies': 5},
]

for book in books:
    if book['copies'] > 0:
        print(f"{book['title']} is available.")
    elif book['copies'] == 0:
        print(f"{book['title']} is currently out of stock.")

print("Finished checking book availability.")
