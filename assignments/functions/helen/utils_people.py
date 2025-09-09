"""Reusable people utilities for Q5."""

from typing import Any, Dict

def full_name(first: str, last: str, middle: str = "") -> str:
    """Return a neatly formatted full name."""
    if middle:
        return f"{first.title()} {middle.title()} {last.title()}"
    return f"{first.title()} {last.title()}"

def build_profile(first: str, last: str, **info: Any) -> Dict[str, Any]:
    """Return a user profile with required names and any extra fields."""
    profile: Dict[str, Any] = {
        "first_name": first.title(),
        "last_name": last.title(),
    }
    for k, v in info.items():
        profile[k] = v
    return profile
