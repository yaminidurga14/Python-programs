def majority_element(a):
    count={}
    n=len(a)
    for num in a:
        count[num]=count.get(num,0)+1
        if count[num] > n // 2:
            return num
# Example usage
A = [2, 1, 2]
print("Majority Element:", majority_element(A))  # Output: 2
