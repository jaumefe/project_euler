# Problema 2 Project Euler. Trobar la suma dels números parells de la sèrie de Fibonacci fins a 40000000
fibo_ant = 1
fibo = 2
fibo_temp = 0
sum = 0

while fibo <= 4000000:
    if fibo % 2 == 0:
        sum += fibo
    fibo_temp = fibo
    fibo += fibo_ant
    fibo_ant = fibo_temp
print(sum)
