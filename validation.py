import re

def validate_age(age):
    try:
        age = int(age)
        return 1 <= age <= 120
    except ValueError:
        return False

def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10



