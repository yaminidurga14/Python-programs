import random
def randon_unique_last(arr):
    unique_elements=[]
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    randomized_list=[]
    while len(unique_elements)>0:
        random_index=random.randint(0,len(unique_elements)-1)
        randomized_list.append(unique_elements[random_index])
        del unique_elements[random_index]
    return randomized_list

a = [1, 2, 5, 3, 4, 6, 7, 8, 8, 8, 8, 9, 9, 9]
result =randon_unique_last(a)
print(result)