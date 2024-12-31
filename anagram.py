def anagram(str1,str2):
    return sorted(str1) ==sorted(str2)
str1 = input("Enter the first string: ") 
str2 = input("Enter the second string: ")
if anagram(str1,str2):
    print("anagram")
else:
    print("not")