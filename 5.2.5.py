n=int(input())
a=[]
count=0
if(n<=0):
    print("Invalid input")
else:
    for i in range (0,n):
        x=int(input())
        a.append(x)

for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]==a[j]):
            count=count+1
if(count==0):
    print("Array elements are not repeted")
else:
    print("The repetitive element : ")
    for i in range(0,n):
        for j in range(i+1,n):
             if(a[i]==a[j]):
                 print(a[j])
