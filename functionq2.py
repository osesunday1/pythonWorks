# q2.py
# This file defines build_person() which returns a dictionary.
# Remember: functions usually RETURN values so they can be reused in different contexts,
# while PRINT is mainly for showing results to the user.

def build_person(first_name, last_name, age=None, occupation=None):
    """
    Build a dictionary containing a person's details.
    Only include 'age' and 'occupation' if provided.
    """
    person = {
        "first": first_name.title(),
        "last": last_name.title()
    }
    if age is not None:
        person["age"] = age
    if occupation is not None:
        person["occupation"] = occupation
    return person  # we return so the value can be used elsewhere (not just displayed)


if __name__ == "__main__":
    # Case (a) no optional values
    print(build_person("ada", "lovelace"))

    # Case (b) only age
    print(build_person("alan", "turing", age=41))

    # Case (c) age and occupation
    print(build_person("grace", "hopper", age=85, occupation="computer scientist"))
