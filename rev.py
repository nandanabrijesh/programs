n=(int(input("number")))
rev=0
while(n!=0):
    s=n%10
    rev=rev*10+s
print(rev,"is reverse")