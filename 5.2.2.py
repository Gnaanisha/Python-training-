n=int(input())
li=[]
for i in range (0,n):
    a=int(input())
    li.append(a)
l=len(li)
temp=0
for i in range(0,l):
    for j in range (i+1,l):
        if(li[i]>li[j]):
            temp=li[j]
            li[j]=li[i]
            li[i]=temp
print("Array sorted in ascending order = ")
for i in range(0,l):
    print(li[i],end=" ")

