def flip_diagonally(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix


matrix1 = [
    [1, 0],
    [0, 1]
]

matrix2 = [
    [1, 0],
    [1, 0]
]

print("Flipped Matrix 1:")
print(flip_diagonally(matrix1))  # Output: [[1, 0], [0, 1]]
print("\nFlipped Matrix 2:")
print(flip_diagonally(matrix2))  # Output: [[1, 1], [0, 0]]
