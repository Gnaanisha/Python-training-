n=int(input())
s=0
a=[]
b=[]
for i in range (0,n):
    x=int(input())
    a.append(x)
for i in range (0,n):
    y=int(input())
    b.append(y)
if(a[i]==b[i]):
    print("Both arrays are equal")
else:
    print("Both arrays are not equal")
