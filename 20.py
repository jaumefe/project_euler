# Problema 20
from math import factorial
num = 100
result = 0
sum = 0

result = factorial(num)
for i in range(len(str(result))):
    sum += int(str(result)[i])
print(sum)
