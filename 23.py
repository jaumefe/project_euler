# Problema 23
from math import sqrt, floor
import time
start_time = time.time()

sumAbundant = 0
abundantNumbers = []
abundantNumbersSum = []
sum = 0
isRepeated = False

# Calcula els divisors i comprova si un número és abundant i si ho és el guarda en un vector
for i in range(1, 28123+1):
    sum += i
    sum1 = 0
    num = i
    for divisors in range(1, floor(sqrt(num)) + 1):
        if num % divisors == 0:
            if (divisors == sqrt(num)) or (divisors == 1):
                sum1 += divisors
            else:
                sum1 += divisors + num//divisors
    if sum1 > num:
        abundantNumbers.append(num)

# Sumem dos números no abundants i guardem la suma sempre que siga inferior a 28123
for i in range(len(abundantNumbers)):
    for j in range(i, len(abundantNumbers)):
        if (abundantNumbers[i] + abundantNumbers[j]) <= 28123:
            abundantNumbersSum.append(abundantNumbers[i] + abundantNumbers[j])

# Ordenem els números
abundantNumbersSum.sort()

# Sumem els números sempre que siguen diferent de l'element anterior
for i in range(len(abundantNumbersSum)):
    if abundantNumbersSum[i] != abundantNumbersSum[i-1]:
        sumAbundant += abundantNumbersSum[i]
print(sum - sumAbundant)
print("Execution time: ", time.time() - start_time, "s")