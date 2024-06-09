n=int(input())
li=[]
for i in range (0,n):
    x=int(input())
    li.append(x)
    print(f"Enter element{i} : ",x)
a=li[0]
for i in range (0,n):
    if(li[i]>a):
        a=li[i]
print("Largest element: ",a)
b=li[0]
for i in range (0,n):
    if(li[i]<b):
        b=li[i]
print("Smallest element: ",b)
