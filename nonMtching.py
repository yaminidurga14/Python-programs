def find_non_matching_characters(str1, str2):
    non_matching=[]
    if len(str1)!=len(str2):
        return "Strings must have the same length for comparison."
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            non_matching.append(str1[i]) 
            non_matching.append(str2[i])
    return non_matching
string1 = input("Enter the first string: ") 
string2 = input("Enter the second string: ") 
 
non_matching_chars = find_non_matching_characters(string1, string2) 
if non_matching_chars: 
    print("Non-matching characters:", ' '.join(non_matching_chars)) 
else: 
    print("The strings are identical.")