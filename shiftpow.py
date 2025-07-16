n=int(input())
i=0
while(1<<i <=n):
    if(1<<i==n):
        print("power")
        break
    i+=1
else:
    print("not power")