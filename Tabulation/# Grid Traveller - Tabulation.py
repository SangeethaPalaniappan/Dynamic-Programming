# Grid Traveller - Tabulation

m = int(input("row : "))
n = int(input("col : "))
matrix = []
for i in range(m + 1):
    arr = []
    for j in range(n + 1):
        arr.append(0)
    matrix.append(arr)    
#print(matrix)        
matrix[0][0] = 1
#print(matrix)
for i in range(m):
    for j in range(1, n+1):
        #print(i, j-1)
        matrix[i][j] += matrix[i][j-1]
        matrix[i + 1][j - 1] += matrix[i][j-1]

print(matrix[m-1][n-1])