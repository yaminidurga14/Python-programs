def remove_duplicates(arr):
    unqiue=[]
    for item in arr:
        if item not in unqiue:
            unqiue.append(item)
    return unqiue
arr = [1, 2, 3, 2, 4, 5, 3] 
arr_without_duplicates = remove_duplicates(arr) 
print("Array without duplicates:", arr_without_duplicates)