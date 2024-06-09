n=int(input())
m=int(input())
a=[]
b=[]
for i in range (0,n):
    x=int(input())
    a.append(x)
for i in range (0,m):
    y=int(input())
    b.append(y)
maxi=a[0]
for i in range(0,n):
    if(a[i]>maxi):
        maxi=a[i]
mini=b[0]
for i in range(0,m):
    if(b[i]<mini):
        mini=b[i]
print(f"max element in first array is {maxi} and min element in second array is {mini}")
print(f"The product of these two is {maxi*mini}")
