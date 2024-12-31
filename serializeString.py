def serialize_string_array(A):
    serialized_result = ""
    for string in A:
        serialized_result += string + str(len(string)) + "~"
    return serialized_result

# Example Inputs
A1 = ['scaler', 'academy']
A2 = ['interviewbit']

# Example Outputs
print(serialize_string_array(A1))  # Output: 'scaler6~academy7~'
print(serialize_string_array(A2))  # Output: 'interviewbit12~'
