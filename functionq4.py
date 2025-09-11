# q4.py
# This file demonstrates:
# 1. make_pizza(size, *toppings) -> returns a formatted string summary of a pizza order.
# 2. build_profile(first, last, **info) -> returns a dictionary with personal info.

def make_pizza(size, *toppings):
    """
    Return a formatted string summarizing the pizza order.
    """
    summary = f"Pizza size: {size} inch\nToppings:"
    if toppings:
        for topping in toppings:
            summary += f"\n- {topping}"
    else:
        summary += "\n- no toppings"
    return summary


def build_profile(first, last, **info):
    """
    Build a profile dictionary with required first/last names
    and any number of extra keyword arguments.
    """
    profile = {
        "first_name": first.title(),
        "last_name": last.title()
    }
    profile.update(info)  # add extra fields
    return profile


if __name__ == "__main__":
    # --- Demonstrate make_pizza ---
    print("=== Pizza Orders ===")
    print(make_pizza(12, "pepperoni", "mushrooms", "cheese"))
    print()
    print(make_pizza(8))  # no toppings

    # --- Demonstrate build_profile ---
    print("\n=== User Profiles ===")
    print(build_profile("ada", "lovelace", location="London", field="Mathematics"))
    print(build_profile("grace", "hopper", age=85, occupation="Computer Scientist", hobby="Sailing"))
