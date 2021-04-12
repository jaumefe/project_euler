# Problema 16
base = 2
exponent = 1000
sum = 0
A = base ** exponent

cadena = str(A)

for i in range(len(cadena)):
    sum += int(cadena[i])

print(sum)
