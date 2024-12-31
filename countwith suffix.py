#  a=start , b= end range c=last char to find in range
#  if c is sibgle digit


def count_numbers_with_last_digit(A, B, C):
    count = 0
    for num in range(A, B + 1):
        if num % 10 == C:
            count += 1
    return count

# Example Inputs
A1, B1, C1 = 11, 111, 1
A2, B2, C2 = 1, 9, 0

print(count_numbers_with_last_digit(A1, B1, C1))  # Output: 11
print(count_numbers_with_last_digit(A2, B2, C2))  # Output: 0


# if c is more than one digit


# def count_numbers_with_suffix(A, B, C):
#     count = 0
#     c_str = str(C)  # Convert C to a string
#     for num in range(A, B + 1):
#         if str(num).endswith(c_str):  # Check if the number ends with C
#             count += 1
#     return count

# # Example Inputs
# A1, B1, C1 = 11, 111, 1        # Single-digit C
# A2, B2, C2 = 10, 100, 12       # Double-digit C
# A3, B3, C3 = 100, 2000, 123    # Triple-digit C

# print(count_numbers_with_suffix(A1, B1, C1))  # Output: 11
# print(count_numbers_with_suffix(A2, B2, C2))  # Output: 0
# print(count_numbers_with_suffix(A3, B3, C3))  # Output: 1
