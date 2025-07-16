n=int(input("enter a number"))
sum=0
temp=n
while temp> 0:
    num=temp%10
    sum=sum+num**3
    temp=temp//10
if(n==sum):
    print("armstrong number")
else:
    print("not armstrong") 