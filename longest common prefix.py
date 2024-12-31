def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix=strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example usage
A1 = ["abcdefgh", "aefghijk", "abcefgh"]
A2 = ["abab", "ab", "abcd"]

print("Output 1:", longest_common_prefix(A1))  # Output: "a"
print("Output 2:", longest_common_prefix(A2))   # Output: "ab"




# Example:

# First Iteration:

# prefix = "abcdefgh"
# string = "aefghijk"
# "aefghijk".startswith("abcdefgh") → False
# prefix = "abcdefg"
# "aefghijk".startswith("abcdefg") → False
# Repeat until prefix = "a".
# "aefghijk".startswith("a") → True.
# Second Iteration:

# prefix = "a"
# string = "abcefgh"
# "abcefgh".startswith("a") → True