arr=[7,9,4,3,6,8]
n=[]
s=0
for i in range(1,len(arr),2):
        n.append(arr[i])
for i in n:
        s=s+i
print(s)