text=input("enter a string:")
vowels=0
consonents=0
for char in text:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels+1
        else:
            consonents+=1
print(vowels)
print(consonents)