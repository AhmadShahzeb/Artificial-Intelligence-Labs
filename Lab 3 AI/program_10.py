# rows and columns

m = int(input("Rows: "))
n = int(input("Columns: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    matrix.append(row)

print(matrix)