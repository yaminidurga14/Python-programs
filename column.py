def column(matrix):
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j], end="\t")
        print()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
column(matrix)
