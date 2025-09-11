# q1.py
# This file contains two functions:
# 1. greet_user(username) -> returns a greeting string.
# 2. full_name(first, last, middle='') -> returns a neatly formatted full name.
# At the bottom, we test both functions.

def greet_user(username):
    """
    Return a greeting message for the given username.
    The name will be capitalized using title().
    """
    return f"Hello, {username.title()}!"

def full_name(first, last, middle=''):
    """
    Return a neatly formatted full name.
    Middle name is optional and handled properly (no extra spaces if omitted).
    """
    if middle:  # middle is not empty
        return f"{first.title()} {middle.title()} {last.title()}"
    else:
        return f"{first.title()} {last.title()}"

# Demonstration block
if __name__ == '__main__':
    # Test greet_user
    print(greet_user("jesse"))
    print(greet_user("ada"))
    print(greet_user("marie"))

    # Test full_name
    print(full_name("ada", "lovelace"))
    print(full_name("john", "doe", "paul"))
    print(full_name("grace", "hopper"))
