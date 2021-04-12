# Problema 24
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(A)
c = []
res = ['[0123456789]']

for i in range(n):
    c.append(0)
# Algoritme de Heap per a calcular permutacions
i = 0
while i < n:
    A_temp = []
    if c[i] < i:
        if i % 2 == 0:
            A[0], A[i] = A[i], A[0]
        else:
            A[c[i]], A[i] = A[i], A[c[i]]
        for j in range(len(A)):
            A_temp.append(A[j])
        A_temp = str(A_temp).replace(', ', '')
        res.append(A_temp)
        c[i] += 1
        i = 0
    else:
        c[i] = 0
        i += 1
res.sort()
print(res[1000000-1])
