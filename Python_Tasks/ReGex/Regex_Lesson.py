###

import re
names_list = [
    "James Stewart Smith",
    "Emily Johnson",
    "Michael Brown Samson",
    "Sarah Davis",
    "William Miller",
    "Olivia Wilson Udevar",
    "David Moore Davidson",
    "Sophia Taylor Kennedy",
    "Christopher Anderson",
    "Isabella Thomas"
]

# People with first and last name only
def first_last_name(names_list):
    regex = r'^\w+ \w+$'
    for name in names_list:
        result = re.search(regex, name)
        if result:
            print(name)
first_last_name(names_list)

print()

# Search for word char sequence starting with C
def name_with_C_letters(names_list):
    regex = r'C\w*'
    for name in names_list:
        match = re.search(regex, name)
        if match:
            print(name)
name_with_C_letters(names_list)

print()

# Test for first and last name
def first_last_name_only(names_list):
    regex = r'^\s+ \w+$'
    for name in names_list:
        result = re.search(regex, name)
        if result:
            print(name)
first_last_name_only(names_list)
