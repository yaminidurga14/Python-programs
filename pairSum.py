def pairSum(arr,target):
    pairs=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                pairs.append((arr[i],arr[j]))
    return pairs
arr=[1,2,3,4]
target=7
result=pairSum(arr,target)
print(result)