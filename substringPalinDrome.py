def is_palindrome(s):
    return s == s[::-1]  # Check if the string is equal to its reverse

def count_palindromic_substrings(A):
    n = len(A)
    count = 0

    for i in range(n):
        for j in range(i, n):  # Generate all substrings starting at i
            if is_palindrome(A[i:j + 1]):  # Check if substring A[i:j+1] is a palindrome
                count += 1

    return count

print(count_palindromic_substrings("aba"))  # Output: 4
print(count_palindromic_substrings("abcd")) # Output: 4
