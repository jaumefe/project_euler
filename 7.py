# Problema 7. Calcular el número primer 10001
from math import floor, sqrt
import time
start_time = time.time()

order = 0
num = 1000000
prime = 0

for i in range(2, num):
    while order < 10001:
        isPrime = True
        for divisor in range(2, floor(sqrt(i)) + 1):
            if i % divisor == 0:
                isPrime = False
                break
        if isPrime:
            order += 1
            prime = i
        break
    if order == 10001:
        break
print(prime)
print("Execution time: ", time.time() - start_time, "s")









