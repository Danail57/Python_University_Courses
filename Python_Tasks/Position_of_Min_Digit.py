###  Да се състави програма,
# която намира номера на
# най-малката цифра в
# зададено цяло число.

def min_index_position_digit(number):
    number = str(abs(number))
    min_digit = int(number[0])
    min_position = 1

    for index, char in enumerate (number):
        digit = int(char)
        if digit < min_digit:
            min_digit = digit
            min_position = index + 1
    return min_position
n = int(input())
result = min_index_position_digit(n)
print("The position of the smallest digit:", result)
