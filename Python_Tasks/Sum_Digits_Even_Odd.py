def even_sum_digits(number):
    sum_even_digit = 0
    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            sum_even_digit += digit
    return sum_even_digit


def odd_sum_digits(number):
    sum_odd_digit = 0
    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 1:
            sum_odd_digit += digit
    return sum_odd_digit


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

even_sum = even_sum_digits(number1) + even_sum_digits(number2)
odd_sum = odd_sum_digits(number1) + odd_sum_digits(number2)

print("Even sum digits: ", even_sum)
print("Odd sum digits: ", odd_sum)
