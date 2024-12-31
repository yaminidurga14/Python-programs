def check_permutation_sort(A, B):
    
    if len(A) != len(B):
        return 0

    
    if sorted(A) == sorted(B):
        return 1
    return 0
print(check_permutation_sort('scaler', 'relasc'))  # Output: 1
print(check_permutation_sort('scaler', 'interviewbit'))  # Output: 0
