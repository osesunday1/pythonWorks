"""Reusable pizza utilities for Q5."""

from typing import List

def make_pizza(size: int, *toppings: str) -> str:
    """
    Return a multi-line string describing the pizza order.
    """
    lines: List[str] = [f"Pizza size: {size}\"", "Toppings:"]
    if toppings:
        for t in toppings:
            lines.append(f"- {t}")
    else:
        lines.append("- no toppings")
    return "\n".join(lines)
