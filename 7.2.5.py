str1=input()
li=list(str1)
l=len(li)
temp=0
for i in range(0,l):
    for j in range (i+1,l):
        if(li[i]>li[j]):
            temp=li[j]
            li[j]=li[i]
            li[i]=temp
a=''.join(li)
print("The output string : ",a)
