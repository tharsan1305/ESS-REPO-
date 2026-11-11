import re

# Username validation
def validate_username(username):

    if not username:
        return False

    if not re.fullmatch(r"[A-Za-z0-9_]{3,15}", username):
        return False

    return True


# Password validation
def validate_password(password):

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    return True


# Security test cases
test_cases = [
    ("student123", "Student123", True),
    ("ab", "Student123", False),
    ("student@123", "Student123", False),
    ("student123", "pass", False),
    ("student123", "STUDENT123", False)
]

print("===== SECURE TEST CASES =====")

for username, password, expected in test_cases:

    result = (
        validate_username(username)
        and validate_password(password)
    )

    if result == expected:
        print("PASS:", username, password)
    else:
        print("FAIL:", username, password)

print("=============================")
print("TESTING COMPLETED")

