def climb_stairs(a):
    if a==1:
        return 1
    if a==2:
        return 2
    
    first=1
    second=2

    for i in range(3,a+1):
        current=first+second
        first=second
        second=current

    return second
A1=2
A2=5

print("Ways to climb", A1, "steps:", climb_stairs(A1)) 
print("Ways to climb", A2, "steps:", climb_stairs(A2)) 




# Explanation
# Recursive Relation
# ways
# (
# n
# )
# =
# ways
# (
# n
# −
# 1
# )
# +
# ways
# (
# n
# −
# 2
# )
# ways(n)=ways(n−1)+ways(n−2)
# Base cases:
# ways
# (
# 1
# )
# =
# 1
# ways(1)=1 (only 1 way: [1])
# ways
# (
# 2
# )
# =
# 2
# ways(2)=2 (two ways: [1,1] and [2])
# Example Walkthrough
# For 
# A
# =
# 3
# A=3:

# ways
# (
# 3
# )
# =
# ways
# (
# 2
# )
# +
# ways
# (
# 1
# )
# ways(3)=ways(2)+ways(1)
# ways
# (
# 2
# )
# =
# 2
# ways(2)=2, 
# ways
# (
# 1
# )
# =
# 1
# ways(1)=1
# ways
# (
# 3
# )
# =
# 2
# +
# 1
# =
# 3
# ways(3)=2+1=3
# Ways: [1,1,1], [1,2], [2,1]
# For 
# A
# =
# 4
# A=4:

# ways
# (
# 4
# )
# =
# ways
# (
# 3
# )
# +
# ways
# (
# 2
# )
# ways(4)=ways(3)+ways(2)
# ways
# (
# 3
# )
# =
# 3
# ways(3)=3, 
# ways
# (
# 2
# )
# =
# 2
# ways(2)=2
# ways
# (
# 4
# )
# =
# 3
# +
# 2
# =
# 5
# ways(4)=3+2=5
# Ways: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]