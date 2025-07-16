a=[2,8,7,6]
first =second=float('-inf')
for i in a:
    if i>first:
        second=first
        first=i
    elif first> i > second:
        second=i
if second==float('-inf'):
    print("not exist")
else:
    print("secon largest number is ",second)   