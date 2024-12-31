def set_matrix_zeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Use two sets to track rows and columns that need to be zeroed
    zero_rows = set()
    zero_cols = set()

    # Step 1: Identify rows and columns that should be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Step 2: Zero out the identified rows
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Step 3: Zero out the identified columns
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0

    return matrix

# Example usage
A1 = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
A2 = [[1, 0, 1], [1, 1, 1], [1, 0, 1]]

print("Output 1:")
print(set_matrix_zeroes(A1))
print("Output 2:")
print(set_matrix_zeroes(A2))
