###   Да се състави програма, която проверява дали
# се среща зададен символ в даден символен низ.

def occurrence_of_a_symbol(string, target_char):
    count = 0
    for char in string:
        if char == target_char:
            count += 1
    if count > 0:
        return f'The symbol "{target_char}" occurs {count} times.'
    else:
        return f'The symbol "{target_char}" does not occur.'

text = input("Write a string: ")
searched_char = input("Write the searched char: ")
print(occurrence_of_a_symbol(text, searched_char))
