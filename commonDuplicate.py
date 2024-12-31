from collections import Counter
def common_element(a,b):
    freq_a=Counter(a)
    freq_b=Counter(b)
    result=[]
    for key in freq_a:
        if key in freq_b:
            common_count=min(freq_a[key],freq_b[key])
            result.extend([key]*common_count)
            return result
        
# Example Input
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
print(common_element(A, B))  # Output: [1, 2, 2]




# Counting Frequencies:

# freq_A = {1: 2, 2: 2}
# freq_B = {2: 2, 3: 1, 1: 1}
# Loop Iteration:

# For key = 1:
# Exists in freq_B.
# common_count = min(2, 1) = 1.
# Add [1] to result.
# result = [1].
# For key = 2:
# Exists in freq_B.
# common_count = min(2, 2) = 2.
# Add [2, 2] to result.
# result = [1, 2, 2].
# Return:

# Final result = [1, 2, 2].
