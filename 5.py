# Problema 5 Project Euler. Mínim comú múltiple dels números de l'1 al 20

l = range(1, 21)

# Càlcul del mínim comú múltiple dels dos primers membres
num1 = l[0]
num2 = l[1]

if num1 > num2:
    num = num1
    den = num2
else:
    num = num2
    den = num1
rem = num % den
while rem != 0:
    num = den
    den = rem
    rem = num % den
gcd = den
lcm = int(int(num1 * num2)/int(gcd))

# Càlcul del mínim comú múltiple del mcm dels dos primers nombres amb el tercer de la llista. I així amb tots els nombres
for i in range(2, 20):
    num1 = lcm
    num2 = l[i]
    if num1 > num2:
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
print(lcm)