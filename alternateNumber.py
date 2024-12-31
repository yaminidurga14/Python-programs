def printAlternateNumber(arr):
    for i in range(0,len(arr),2):
        print(arr[i])
n=int(input("Enter the number of elemnets:"))
arr=[]
print("Enter the elements of the array:")
for _ in range(n):
    arr.append(int(input()))
printAlternateNumber(arr)