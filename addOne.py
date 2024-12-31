def add_one(digits):
    # Convert the list of digits to a number
    num = int(''.join(map(str, digits)))
    # Add 1 to the number
    num += 1
    # Convert the result back to a list of digits
    return [int(digit) for digit in str(num)]

# Example usage
input_digits = [1, 2, 3]
result = add_one(input_digits)
print("Output:", result)  # Output: [1, 2, 4]
