#Problema 4. Trobar el número palíndrom més gran resultat de multiplicar dos números de tres xifres
res_ant = 0
palindrome = 0

for m1 in range(100, 1000):
    for m2 in range(100, 1000):
        res = m1 * m2
        car_res = str(res)
        inversion = ''
        for caracter in car_res:
            inversion = caracter + inversion
        if (car_res == inversion) and (res > res_ant):
            palindrome = res
            res_ant = res
print(palindrome)
