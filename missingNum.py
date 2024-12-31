def find_missing_number(arr): 
    n = 100 
    expected_sum = (n * (n + 1)) // 2 
    actual_sum = sum(arr) 
    missing_number = expected_sum - actual_sum 
    return missing_number
integer_array = list(range(1, 101))  # Creating an array from 1 to 100 
integer_array.remove(42)
missing_number = find_missing_number(integer_array) 
print("Missing number:", missing_number)