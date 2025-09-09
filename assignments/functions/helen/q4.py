"""Q4 — Flexible Arguments (*args and **kwargs)

Functions:
- make_pizza(size, *toppings): return a multi-line summary of the order.
  If no toppings given, include a "- no toppings" line.
- build_profile(first, last, **info): return a dict with first_name, last_name,
  plus any extra keyword fields in info.

Teaches:
- Using *args for arbitrary positional arguments.
- Using **kwargs for arbitrary keyword arguments.
- Clear return values and readable formatting.
"""

from typing import Any, Dict

def make_pizza(size: int, *toppings: str) -> str:
    """
    Return a multi-line string describing the pizza order.
    First line: size information.
    Following lines: bulleted list of toppings (or '- no toppings' if none).
    """
    lines = [f"Pizza size: {size}\"", "Toppings:"]
    if toppings:
        for t in toppings:
            lines.append(f"- {t}")
    else:
        lines.append("- no toppings")
    return "\n".join(lines)


def build_profile(first: str, last: str, **info: Any) -> Dict[str, Any]:
    """
    Return a user profile dictionary with required names and any extra fields.
    """
    profile: Dict[str, Any] = {
        "first_name": first.title(),
        "last_name": last.title(),
    }
    # Merge extra keyword pairs
    for k, v in info.items():
        profile[k] = v
    return profile


if __name__ == "__main__":
    # --- make_pizza demos ---
    many = make_pizza(14, "pepperoni", "mushrooms", "olives", "green peppers")
    none = make_pizza(12)
    print(many)
    print()
    print(none)

    # --- build_profile demos (using your preferred name) ---
    p1 = build_profile("helen", "mohammed",
                       middle="Rukkayat", role="DevOps Engineer", location="Columbia, MD")
    p2 = build_profile("helen", "mohammed")  # no extras
    print()
    print(p1)
    print(p2)
