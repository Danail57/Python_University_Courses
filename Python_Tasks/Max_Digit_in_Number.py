def max_digit_in_number(number):
    max_digit = 0
    for digit in str(number):
        digit = int(digit)
        if digit > max_digit:
            max_digit = digit
    return max_digit
number = int(input("Enter a number: "))
print(max_digit_in_number(number))