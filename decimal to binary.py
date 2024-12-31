def decimal_to_binary(N):
   
    if N == 0:
        return "0"

    
    binary_representation = ""

   
    while N > 0:
        # Append the remainder of N % 2 to the binary representation
        binary_representation = str(N % 2) + binary_representation
     
        N = N // 2

    return binary_representation

N = 6
print(f"Binary form of {N} is {decimal_to_binary(N)}")  # Output: 110
