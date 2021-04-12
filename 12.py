# Problema 12
from math import sqrt, floor
divisors = 0
tri = 1
num = 2

while divisors*2 < 500:
    divisors = 0
    for divisor in range(2, floor(sqrt(tri)) + 1):
        if tri % divisor == 0:
            divisors += 1
    tri += num
    num += 1
print(tri-num+1)
