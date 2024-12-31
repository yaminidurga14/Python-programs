def pair_with_diff(a, b):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
           
            if abs(a[i] - a[j]) == b:
                return 1
    return 0

# Example Usage
A1 = [5, 10, 3,2, 50, 80]
B1 = 78
A2 = [-10, 20]
B2 = 30

print("Output 1:", pair_with_diff(A1, B1))  # Output: 1
print("Output 2:", pair_with_diff(A2, B2))  # Output: 1
