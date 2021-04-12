#Problema 9
res = 0

for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if (a < b < c) and (a ** 2 + b ** 2 == c ** 2):
                if a + b + c == 1000:
                    res = a*b*c

print(res)
