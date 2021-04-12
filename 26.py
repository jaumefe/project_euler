# Problema 26
# Determinar el nombre de decimals que ens faran falta
from decimal import *
getcontext().prec = 100

for i in range(2, 1000):
    a = str(Decimal(1) / Decimal(i))
    