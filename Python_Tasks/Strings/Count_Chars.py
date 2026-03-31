### Count all letters, digits,
# and special symbols from a given string

def count_characters(string):
    count_chars = 0
    count_digits = 0
    count_special_symbols = 0
    for char in string:
        if char.isdigit():
            count_digits += 1
        elif char.isalpha():
            count_chars += 1
        else:
            count_special_symbols += 1
    return (f"Chars -> {count_chars}\n"
            f"Digits -> {count_digits}\n"
            f"Special symbols -> {count_special_symbols}\n")

text = input("Write a string: ")
print(count_characters(text))
