### Write a Python program to validate an email address
# using a regular expression. Prompt the user to enter
# an email address and check if it is valid.

import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True
    else:
        return False

user_email = input("Write an email: ")
if validate_email(user_email):
    print(f"This email '{user_email}' is valid.")
else:
    print(f"This email '{user_email}' is invalid.")
