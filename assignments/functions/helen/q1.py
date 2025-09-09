"""Q1 — Greet & Format (returns, parameters, optional middle).

Functions:
- greet_user(username): return "Hello, <Name>!" with title-cased name.
- full_name(first, last, middle=''): return a neatly formatted full name,
  handling the optional middle name without extra spaces.
"""

def greet_user(username: str) -> str:
    """
    Return a greeting like "Hello, Jesse!".
    We return (not print) so the caller can reuse the string elsewhere.
    """
    return f"Hello, {username.title()}!"


def full_name(first: str, last: str, middle: str = "") -> str:
    """
    Return a neatly formatted full name.
    If middle is empty, don't add extra spaces.
    """
    if middle:
        return f"{first.title()} {middle.title()} {last.title()}"
    return f"{first.title()} {last.title()}"


if __name__ == "__main__":
    # --- Demo calls (prints are only for demonstration when running this file) ---
    print(greet_user("jesse"))
    print(greet_user("helen"))

    print(full_name("helen", "mohammed"))
    print(full_name("helen", "mohammed", "rukkayat"))
    print(full_name("ada", "obi"))

