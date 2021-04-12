# Problema 27
from math import sqrt, floor

nmax = 0
amax = 0
bmax = 0

for a in range(-1000 + 1, 1000):
    for b in range(-1000, 1000 + 1):
        isPrime = True
        n = 0
        num = n ** 2 + a * n + b
        while isPrime:

            if num > 3:
                for divisor in range(2, floor(sqrt(num)) + 1):
                    num = n ** 2 + a * n + b
                    if num % divisor == 0:
                        isPrime = False
                        break
                    else:
                        n += 1
            else:
                isPrime = False
        if n > nmax:
            nmax, amax, bmax = n, a, b
print(amax * bmax)
