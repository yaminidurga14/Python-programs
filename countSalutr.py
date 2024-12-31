def count_salutes(A):
    count_right = 0  # Number of soldiers walking to the right
    salutes = 0      # Total salutes

    for char in A:
        if char == '>':
            count_right += 1
        elif char == '<':
            salutes += count_right  # All soldiers walking to the right will cross this one
    
    return salutes
A = '>>><<<'
b = '<>'
c = '><><'
print(count_salutes(A))  # Output: 9
print(count_salutes(b))  #0
print(count_salutes(c))  #3