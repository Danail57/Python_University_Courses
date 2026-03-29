###   Да се състави програма,
# която преброява символите
# в зададен символен низ.

def count_symbols(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count

text = input("Write a string: ")
print(count_symbols(text))
