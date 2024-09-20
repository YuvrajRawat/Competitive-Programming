class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def display(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

    def spiral_order(self):
        matrix_copy = [row[:] for row in self.matrix]  # Copy to avoid modifying the original matrix
        result = []
        while matrix_copy:
            # Add the first row
            result.extend(matrix_copy.pop(0))

            # Add the last column
            if matrix_copy and matrix_copy[0]:
                for row in matrix_copy:
                    result.append(row.pop())

            # Add the last row reversed
            if matrix_copy:
                result.extend(matrix_copy.pop()[::-1])

            # Add the first column reversed
            if matrix_copy and matrix_copy[0]:
                for row in reversed(matrix_copy):
                    result.append(row.pop(0))
        return result

def read_matrix():
    print("Enter the matrix in the format: [[1,2,3], [4,5,6], [7,8,9]]")
    matrix_str = input("Enter the matrix: ")
    matrix = eval(matrix_str)  # Using eval to parse the input string as a Python expression
    return matrix

# Main execution block
if __name__ == "__main__":
    user_matrix = read_matrix()
    m = Matrix(user_matrix)

    print("\nOriginal Matrix:")
    m.display()

    print("\nSpiral Order of Matrix:")
    print(m.spiral_order())
