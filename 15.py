# Problema 15
from math import factorial

x = 20
y = 20

combinations = factorial(x+y)/(factorial(x)*factorial(x+y-y))
print(combinations)
