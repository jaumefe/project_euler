# Problema 3 Project Euler. Trobar el factor primer més gran de 600851475143

from math import sqrt, floor
import time
start_time = time.time()

numero = 600851475143
primeFactor = 0

#La prova dels divisors es fa fins a sqrt(numero) seguint: https://en.wikipedia.org/wiki/Primality_test

for factor in range(2, floor(sqrt(numero))):
    isPrime = True
    for divisor in range(2, floor(sqrt(factor))+1):
        if factor % divisor == 0:
            isPrime = False
            break
    if isPrime:
        if numero % factor == 0:
            primeFactor = factor
print(primeFactor)

print("Execution time: ", time.time() - start_time, "s")
