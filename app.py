
import re


def validate_email(email):
    if not isinstance(email, str):
        return False

    return bool(
        re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email)
    )


def validate_student(name, age, email):
    if not isinstance(name, str) or not name.strip():
        return False

    if not isinstance(age, int) or isinstance(age, bool) or age <= 0:
        return False

    return validate_email(email)
