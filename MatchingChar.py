def matchingChar(str1,str2):
    set1=set(str1)
    set2=set(str2)
    matching_chars = set1.intersection(set2)
    print("Matching characters are:", ", ".join(matching_chars))


str1=input()
str2=input()
matchingChar(str1,str2)
