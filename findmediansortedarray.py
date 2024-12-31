def findMedianSortedArrays(num1,num2):
    merged=sorted(num1+num2)
    n=len(merged)
    if n%2==1:
        return merged[n//2]
    else:
        return (merged[n//2-1]+merged[n//2])/2
num1=[1,3]
num2=[2]
print(findMedianSortedArrays(num1,num2))