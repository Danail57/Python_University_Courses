### Да се състави програма, която намира
# разликата между сумата от третите степени
# на четните цифри и сумата от вторите степени
# на нечетните цифри на зададено цяло число.

def difference_third_power_evens(number):
    number = abs(number)
    sum_evens_cubed = 0
    sum_odds_squared = 0

    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            sum_evens_cubed += digit
        else:
            sum_odds_squared += digit
    return sum_evens_cubed - sum_odds_squared

n = int(input())
result = difference_third_power_evens(n)
print("Difference is:", result)
