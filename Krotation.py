def rotate_left(arr,k):
    n=len(arr)
    k%=n
    arr[:]=arr[k:]+arr[:k]
def rotate_right(arr,k):
    n=len(arr)
    k%=n
    arr[:]=arr[-k:]+arr[:-k]
arr=[1,2,3,4,5]
rotate_left(arr,2)
print(arr)
arr=[1,2,3,4,5]
rotate_right(arr,2)
print(arr)
