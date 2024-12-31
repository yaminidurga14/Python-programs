def gcd(a,b):
    while b:
        a,b=b,a%b
        return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
n1 = int(input("Enter the first number: ")) 
n2 = int(input("Enter the second number: ")) 
 
gcd_result = gcd(n1, n2) 
lcm_result = lcm(n1, n2) 
 
print("GCD:", gcd_result) 
print("LCM:", lcm_result)