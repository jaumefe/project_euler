# Problema 10
from math import sqrt, floor

sum = 0

for primes in range(2, 2000000):
    isPrime = True
    for divisor in range(2, floor(sqrt(primes)) + 1):
        if primes % divisor == 0:
            isPrime = False
            break
    if isPrime:
        sum += primes
print(sum)
