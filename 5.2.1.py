n=int(input())
if(n==0):
    print("Invalid size")
else:
    li=[]
    for i in range(0,n):
        x=int(input())
        li.append(x)
    print("Array elements: ")
print("The unique elements found in the array are :") 
for i in range(0,n):
    a=0
    for j in range(0,n):
        if(i!=j):
            if(li[i]==li[j]):
                a=a+1
    if(a==0):
        print(li[i],end=" ")
