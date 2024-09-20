def matrix(m, n):
    full_matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            num = int(input(f"Enter the full_matrix[{i}][{j}] : "))
            row.append(num)
        full_matrix.append(row)
    return full_matrix

def sum2matrix(A, B):
    sum_matrix = []
    for i in range(len(A)):
        column = []
        for j in range(len(A[0])):
            column.append(A[i][j] + B[i][j])
        sum_matrix.append(column)
    return sum_matrix

m = int(input("Enter the row: "))
n = int(input("Enter the coloumn: "))

print("Enter Matrix A")
A = matrix(m, n)
print(A)

print("Enter Matrix B")
B = matrix(m, n)
print(B)

result = sum2matrix(A, B)
print(result)

