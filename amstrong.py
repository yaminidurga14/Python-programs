num=int(input("number"))
num_string=str(num)
num_digits=len(num_string)
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**num_digits
    temp//=10
if num == sum: 
    print("Armstrong") 
else: 
    print("Not Armstrong") 