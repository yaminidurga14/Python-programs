def max_count(A, B, C):
    countA = sum(1 for x in A if x > C)  # Count elements in A greater than C
    countB = sum(1 for x in B if x < C)  # Count elements in B less than C
    return max(countA, countB)  # Return the maximum of the two counts

# Example Input
A1 = [1, 2, 3, 4]
B1 = [5, 6, 7, 8]
C1 = 4

A2 = [1, 10, 100]
B2 = [9, 9, 9]
C2 = 50

print(max_count(A1, B1, C1))  # Output: 0
print(max_count(A2, B2, C2))  # Output: 3
