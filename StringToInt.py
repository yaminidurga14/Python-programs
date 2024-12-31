def extractIntegers(a):
    string_list=a.split(',')
    int_list=[int(num) for num in string_list]
    return int_list
a1="1,2,3"
b1="1,99,3"
print(extractIntegers(a1))
print(extractIntegers(b1))