"""Q2 — Person Builder (return dictionaries with optional fields)

Function:
- build_person(first_name, last_name, age=None, occupation=None): returns a dict with
  keys 'first', 'last', and only includes 'age' and 'occupation' if they are provided (not None).

Return vs print:
- We RETURN the dictionary so other code/tests can use it.
- We only PRINT inside the __main__ demo to show examples when running this file directly.
"""

from typing import Optional, Dict, Any

def build_person(first_name: str, last_name: str,
                 age: Optional[int] = None,
                 occupation: Optional[str] = None) -> Dict[str, Any]:
    """Return a person dictionary; include optional keys only when values are provided."""
    person = {
        "first": first_name.title(),
        "last": last_name.title(),
    }
    if age is not None:
        person["age"] = age
    if occupation is not None:
        person["occupation"] = occupation
    return person


if __name__ == "__main__":
    # Demo: 3 calls — (a) no optionals, (b) only age, (c) age + occupation
    print(build_person("helen", "mohammed"))
    print(build_person("helen", "mohammed", age=28))
    print(build_person("helen", "mohammed", age=28, occupation="DevOps Engineer"))
