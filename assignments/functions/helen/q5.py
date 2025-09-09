"""Q5 — Modules & Imports (same-folder modules)

We will:
- import functions from utils_pizza.py and utils_people.py (same directory)
- demonstrate several import styles and print demo outputs

Note: These modules live in the same folder as q5.py, so we can import them directly.
"""

# --- Import styles ---
# Style 1: from module import function(s)
from utils_pizza import make_pizza
from utils_people import full_name, build_profile

# Style 2: module alias (lets us call module.function)
import utils_pizza as pizza_utils

# (Optional) Style 3: plain import (not strictly needed here, shown for completeness)
import utils_people

if __name__ == "__main__":
    # --- Using Style 1 imports ---
    order_1 = make_pizza(16, "pepperoni", "mushrooms", "olives")
    order_2 = make_pizza(12)  # no toppings
    print(order_1)
    print()
    print(order_2)

    # --- Using Style 2 (alias) ---
    big_order = pizza_utils.make_pizza(18, "beef", "onions", "jalapeños", "extra cheese")
    print()
    print(big_order)

    # --- People utilities (two styles) ---
    # Style 1 direct function imports:
    name = full_name("helen", "mohammed", "rukkayat")
    profile = build_profile("helen", "mohammed", role="DevOps Engineer", city="Columbia")
    print()
    print(name)
    print(profile)

    # Style 3 plain module import: access via the module name
    name2 = utils_people.full_name("ada", "obi")
    profile2 = utils_people.build_profile("ada", "obi", role="QA", city="Baltimore")
    print()
    print(name2)
    print(profile2)
