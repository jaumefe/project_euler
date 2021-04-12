# Problema 14
import time
start_time = time.time()
cadena_max = 0
num = 0

for i in range(2, 1000000):
    n = i
    cadena = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        cadena += 1
    if cadena > cadena_max:
        num = i
        cadena_max = cadena

print(num)
print("Execution time: ", time.time() - start_time, "s")
