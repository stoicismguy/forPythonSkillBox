size = int(input())

def print_matrix(matrix):
    for i in matrix:
        for h in range(len(i)):
            if h != len(i) - 1:
                print(i[h], end=", ")
            else:
                print(i[h])

matrix1 = []
for i in range(size):
    matrix1.append([])

print_matrix(matrix1)
for row in range(size):
    for column in range(size):
        matrix1[row].append(column + 1)

print_matrix(matrix1)
print()
matrix2 = []
for i in matrix1:
    matrix2.append(i.copy())

for row in range(size):
    for column in range(size):
        matrix2[row][column] = row + 1

print_matrix(matrix2)
