def sum_of_numbers(a):
    import re
    numbers=re.findall(r'\d+',a)
    total=sum(int(num) for num in numbers)
    return total
A1 = "a12b34c"
A2 = "123"
print("Output 1:", sum_of_numbers(A1))  # Output: 46
print("Output 2:", sum_of_numbers(A2))  # Output: 123