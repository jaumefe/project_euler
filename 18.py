# Problema 18
triangle = [[75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [95, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [17, 47, 82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [18, 35, 87, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [20, 4, 82, 47, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [19, 1, 23, 75, 3, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [88, 2, 77, 73, 7, 63, 67, 0, 0, 0, 0, 0, 0, 0, 0],
            [99, 65, 4, 28, 6, 16, 70, 92, 0, 0, 0, 0, 0, 0, 0],
            [41, 41, 26, 56, 83, 40, 80, 70, 33, 0, 0, 0, 0, 0, 0],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 0, 0, 0, 0, 0],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 0, 0, 0, 0],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 0, 0, 0],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 0, 0],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 0],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

#triangle = [[8, 0, 0, 0],
#            [-4, 4, 0, 0],
#            [2, 2, 6, 0],
#            [1, 1, 1, 1]]

# La solució que es proposa a continuació, consisteix a anar fent operacions des de la base del triangle.
# Sumarem els elements de la última fila amb els adjacents de la superior. I ens quedarem amb la suma dels quals siga la major
rows = len(triangle)
columns = len(triangle[0])
i = rows - 1

while i != 0:
# for i in range(rows - 1, -1, 1):
    for j in range(columns):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        #if j != 0:
        #    sum1 = triangle[i-1][j] + triangle[i][j-1]
        #else:
        #    sum1 = 0
        sum2 = triangle[i-1][j] + triangle[i][j]
        if j != columns - 1:
            sum3 = triangle[i-1][j] + triangle[i][j+1]
        else:
            sum3 = 0
        if triangle[i-1][j] != 0:
            triangle[i-1][j] = max(sum1, sum2, sum3)
        else:
            triangle[i-1][j] = 0
    i -= 1
print(triangle[0][0])
