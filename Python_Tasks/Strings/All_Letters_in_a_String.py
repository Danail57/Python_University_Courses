### Да се състави програма, която проверява
# дали зададен символен низ съдържа всички букви от а до z.


def has_all_letters(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    for char in alphabet:
        if char not in string:
            return False
    return True

text = input("Enter a string: ")
if has_all_letters(text):
    print("It has all letters")
else:
    print("It does not have all letters")
