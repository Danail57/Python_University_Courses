### Write a Python program that extracts phone numbers
# from a given text string using a regular expression.
# Test it with a sample text containing phone numbers
# in various formats.

import re
def extract_phone_number(text):
    pattern = r'\+?\d{1,3}[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
    return re.findall(pattern, text)

text = input('Write a text with phone numbers: ')
numbers = extract_phone_number(text)
if numbers:
    print("Found numbers: ")
    for number in numbers:
        print(f"{number.strip()}")
else:
    print("No numbers found")
