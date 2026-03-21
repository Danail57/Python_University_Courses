def sum_digits(number):
    sum_digit = 0
    for digit in str(number):
        sum_digit += int(digit)
    return sum_digit
number = int(input("Enter a number: "))
print("Result:", sum_digits(number))