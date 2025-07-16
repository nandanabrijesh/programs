a=int(input("enter 1st side"))
b=int(input("enter 2nd side"))
c=int(input("enter 3rd side"))
if(a==b==c):
    print("equilateral traiangle")
elif(a!=b and a!=c and b!=c ):
    print("scalene")
else:
    print("isosceles")