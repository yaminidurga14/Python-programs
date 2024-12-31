def find_index(my_arr,t):
    if t in my_arr:
        return my_arr.index(t)
    return -1

my_array = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49] 
print("Index position of 25 is:", find_index(my_array, 25)) 
print("Index position of 77 is:", find_index(my_array, 77)) 