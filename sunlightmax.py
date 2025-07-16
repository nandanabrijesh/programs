list=[2,4,7,3,2,8]
sun=[]
max=0
for i in list:
    if i > max:
        sun.append(i)
        max=i
print(sun)