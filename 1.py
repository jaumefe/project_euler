#Problema 1 Project Euler. Trobar la suma del multiples de 3 i 5 fins al 1000
numero = 0
sum = 0

while numero < 1000:
    numero += 1
    if ((numero % 3) == 0) or ((numero % 5) == 0):
        sum += numero
print(sum - numero)