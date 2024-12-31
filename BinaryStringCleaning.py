# Problem Explanation
# You are given a binary string 
# s
# s of length 
# n
# n consisting of only 0s and 1s. Ryan can perform a specific move:

# If there are two consecutive characters 
# s
# [
# i
# ]
# s[i] and 
# s
# [
# i
# +
# 1
# ]
# s[i+1] such that 
# s
# [
# i
# ]
# =
# 1
# s[i]=1 and 
# s
# [
# i
# +
# 1
# ]
# =
# 0
# s[i+1]=0, Ryan can erase exactly one of them.
# After each erasure, the string becomes shorter, and the positions of the characters shift accordingly. Ryan can perform as many moves as he wants until no further moves are possible.

# The goal is to determine the cleanest possible string Ryan can achieve after performing all valid moves:

# The shorter the string, the cleaner it is.
# If two strings have the same length, the lexicographically smaller string is considered cleaner.


def clean_string(s):
    stack=[]
    for char in s:
        if stack and stack[-1]=='1' and stack=='0':
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

input1 = "0001111111"
input2 = "0101"

print("Output 1:", clean_string(input1))  # Output: "0001111111"
print("Output 2:", clean_string(input2))  # Output: "001"