#Problema 7 Project Euler. Calcular la diferència entre el quadrat de la suma i la suma dels quadrats

sumaCuadrados = 0
cuadradoSuma = 0

for sumandos in range(1, 100 + 1):
    sumaCuadrados += sumandos ** 2
    cuadradoSuma += sumandos

res = - sumaCuadrados + cuadradoSuma ** 2
print(res)