n=int(input())
li=[]
a=0
for i in range (0,n):
    x=int(input())
    li.append(x)
se=int(input())
for i in range(0,n):
    if(li[i]==se):
        a=a+1
        break
if(a>0):
    print(f"{se} found at position {i}")
else:
    print(f"{se} not found")
