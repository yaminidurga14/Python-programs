def is_valid_password(A):
    if not (8 <= len(A) <= 15):
        return 0

    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False
    special_characters = {'@', '#', '%', '&', '!', '$', '*'}

    for char in A:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char in special_characters:
            has_special = True

        if has_digit and has_lower and has_upper and has_special:
            return 1

    return 0

A1 = ['S', 'c', 'a', 'l', 'e', 'r', '@', '1']
A2 = ['I', 'n', 't', 'e', 'r', 'v', 'i', 'e', 'w', 'B', 'i', 't']

print("Output 1:", is_valid_password(A1))  # Output: 1
print("Output 2:", is_valid_password(A2))  # Output: 0







# import re

# def is_valid_password(password):

#     password = ''.join(password)


#     pattern = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#%&!$*])[A-Za-z0-9@#%&!$*]{8,15}$"


#     if re.match(pattern, password):
#         return 1
#     return 0

# # Example Usage
# print(is_valid_password(['S', 'c', 'a', 'l', 'e', 'r', '@', '1']))  # Output: 1
# print(is_valid_password(['I', 'n', 't', 'e', 'r', 'v', 'i', 'e', 'w', 'B', 'i', 't']))  # Output: 0
