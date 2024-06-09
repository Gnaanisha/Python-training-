n=int(input())
s=0
li=[]
for i in range (0,n):
    a=int(input())
    li.append(a)
for i in range(0,n):
    s=s+li[i]
print("The sum of array elements = ",s)
