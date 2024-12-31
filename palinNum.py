num = int(input("Enter a number: ")) 
num_str = str(num) 
reversed_num = int(num_str[::-1]) 
 
if num == reversed_num: 
    print("Palindrome") 
else: 
    print("Not Palindrome") 