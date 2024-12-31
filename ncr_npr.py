def factorial(n): 
    if n == 0: 
        return 1 
    return n * factorial(n - 1) 
 
n = int(input("Enter n: ")) 
r = int(input("Enter r: ")) 
 
ncr = factorial(n) // (factorial(r) * factorial(n - r)) 
npr = factorial(n) // factorial(n - r) 
 
print("NCR:", ncr) 
print("NPR:", npr) 