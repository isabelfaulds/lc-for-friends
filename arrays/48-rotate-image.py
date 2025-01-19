class Solution:
    def print_matrix(self, matrix):
        for i in matrix:
            print(i)
        print('\n')

# Using rings
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rings = n + 1 // 2
        for layer in range(rings):
            for i in range(layer, n - layer - 1):
                self.print_matrix(matrix)
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[n - 1 - i][layer]
                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1 - i]
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                matrix[i][n - 1 - layer] = temp
        self.print_matrix(matrix)

# Using transpose
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # column & row width
        for i in range(n): # transpose
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

# Original Matrix:         Transposed Matrix:
# 1  2  3                  1  4  7
# 4  5  6      --->        2  5  8
# 7  8  9                  3  6  9

# Transposed Matrix:         Reversed Transposed Matrix:
# 1  4  7                  7  4  1
# 2  5  8      --->        8  5  2
# 3  6  9                  9  6  3

# odd row counts easily handled