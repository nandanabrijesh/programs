n=int(input("enter a number"))
if(n>0):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    print(fact)