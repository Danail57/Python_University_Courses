### Да се състави програма, която намира
# разликата между сумата от третите степени
# на четните цифри и сумата от вторите степени
# на нечетните цифри на зададено цяло число.

def difference_third_power_evens(number):
    digits = [int(d) for d in str(abs(number))]
    evens = sum(d ** 3 for d in digits if d % 2 == 0)
    odds = sum(d ** 2 for d in digits if d % 2 != 0)
    return evens - odds
n = int(input())
result = difference_third_power_evens(n)
print("Difference is:",result)
