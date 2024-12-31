def is_palin(s):
    s=s.lower()
    s=''.join(e for e in s if e.isalnum())
    return s==s[::-1]
text = input("Enter a string: ") 
if is_palin(text): 
    print("Palindrome") 
else: 
    print("Not Palindrome")