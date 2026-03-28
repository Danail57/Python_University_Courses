### Да се състави програма, която намира
# произведението между сумата на цифрите,
# по-големи от 5, и сумата на цифрите,
# по-малки от 5, на зададено цяло число.

def solution(number):
    number = abs(number)
    sum_greater_than_5 = 0
    sum_less_than_5 = 0

    for digit in str(number):
        digit = int(digit)
        if digit < 5:
            sum_less_than_5 += digit
        elif digit > 5:
            sum_greater_than_5 += digit
    return sum_greater_than_5 * sum_less_than_5

n = int(input())
result = solution(n)
print("Multiplication result is:", result)
