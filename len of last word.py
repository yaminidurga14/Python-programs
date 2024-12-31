def len_of_last_word(s):
    words=s.split()
    if not words:
        return 0
    last_word=words[-1]
    return len(last_word)

# Example Inputs
A1 = " hello world "
A2 = "InterviewBit"

# Example Outputs
print("Output 1:", len_of_last_word(A1))  # Output: 5
print("Output 2:", len_of_last_word(A2))  # Output: 12
