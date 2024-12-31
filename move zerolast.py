def move_zero(a):
    non_zero_index=0
    for i in range(len(a)):
        if a[i]!=0:
            a[non_zero_index],a[i]=a[i],a[non_zero_index]
            non_zero_index+=1
    return a


A1 = [0, 1, 2, 3]
A2 = [1, 0, 0, 0]

# Example Output
print(move_zero(A1))  # Output: [1, 2, 3, 0]
print(move_zero(A2))  # Output: [1, 0, 0, 0]
