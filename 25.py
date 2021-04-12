# Problema 25
import time
start_time = time.time()
Fibo = [1, 1]

while len(str(Fibo[len(Fibo)-1])) != 1000:
    Fibo.append(Fibo[len(Fibo)-1] + Fibo[len(Fibo)-2])

print(len(Fibo))
print("Execution time: ", time.time() - start_time, "s")
