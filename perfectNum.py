def is_perfect(num): 
    divisors_sum = sum([i for i in range(1, num) if num % i == 0]) 
    return num == divisors_sum 
 
n = int(input("Enter a number: ")) 
 
if is_perfect(n): 
    print("Perfect Number") 
else: 
    print("Not a Perfect Number") 