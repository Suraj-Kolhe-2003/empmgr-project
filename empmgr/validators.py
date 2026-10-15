
# empmgr/validators.py
def parse_salary(text):
    """Convert salary text to a valid non-negative number."""
    try:
        salary = float(text)
        if salary < 0:
            return None
        return salary
    except ValueError:
        return None


def is_valid_email(email):
    """Check whether an email has a basic valid format."""
    if email.count("@") != 1:
        return False

    parts = email.split("@")

    if not parts[0] or not parts[1]:
        return False

    if "." not in parts[1]:
        return False

    if parts[1].startswith(".") or parts[1].endswith("."):
        return False

    return True
