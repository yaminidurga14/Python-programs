int_input=int(input("Enter a integer"))

float_input=float(input("Enter a float:"))

string_input=input("enter a string:")


# Getting a list of integers from space-separated input
list_input=list(map(int,input())) #[1, 2, 3, 4, 5]


# Getting multiple values in a single line
a, b, c = map(int, input("Enter three integers separated by spaces: ").split()) #You entered: a = 10, b = 20, c = 30

# Getting a tuple from input
tuple_input = tuple(map(int, input("Enter a tuple of integers (space-separated): ").split())) #You entered the tuple: (7, 8, 9)


# Getting a dictionary from input
n = int(input("Enter the number of key-value pairs for the dictionary: "))
print("Enter the key-value pairs (e.g., key value):")
dictionary = {}

for _ in range(n):
    key, value=input().split()
    dictionary[key]=int(value)
print(dictionary) #{'name': 42, 'age': 25}


# Getting an array as input
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
print("You entered the array:", arr)

# Get the number of inputs
n = int(input("Enter the number of inputs: "))
numbers = []
for _ in range(n):
    num = int(input(f"Enter number {_ + 1}: "))
    numbers.append(num)
print("You entered:", numbers)


# Enter the number of inputs: 3
# Enter number 1: 10
# Enter number 2: 20
# Enter number 3: 30




# Get the number of input arrays
m = int(input("Enter the number of arrays: "))
arrays = []
for i in range(m):
    print(f"Enter elements for array {i + 1} (space-separated):")
    arr = list(map(int, input().split()))
    arrays.append(arr)

print("You entered the following arrays:")
for arr in arrays:
    print(arr)


# Enter elements for array 1 (space-separated):
# 1 2 3
# Enter elements for array 2 (space-separated):
# 4 5 6
# Enter elements for array 3 (space-separated):
# 7 8 9
