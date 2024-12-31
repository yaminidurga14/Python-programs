num = int(input("Enter a number: ")) 
target_digit = int(input("Enter the target digit: ")) 
count = 0 
while num>0:
    digit=num%10
    if digit== target_digit:
        count+=1
    num//=10
print("Count of digit", target_digit, "is:", count)