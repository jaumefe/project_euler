# Problema 21
from math import sqrt, floor

sum = 0
num = 0

for i in range(2, 10000):
    sum1 = 0
    sum2 = 0
    num = i
    for divisors in range(1, floor(sqrt(num)) + 1):
        if num % divisors == 0:
            if (divisors == sqrt(num)) or (divisors == 1):
                sum1 += divisors
            else:
                sum1 += divisors + num//divisors
    if i != sum1:
        for divisors in range(1, floor(sqrt(sum1)) + 1):
            if sum1 % divisors == 0:
                if (divisors == sqrt(sum1)) or (divisors == 1):
                    sum2 += divisors
                else:
                    sum2 += divisors + sum1//divisors
    if sum2 == num:
        sum += sum1 + num
print(sum//2)
