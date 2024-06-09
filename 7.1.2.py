str1= input()
oc=input()
nc=input()
a=list(str1)
for i in range(len(a)):
    if(a[i]==oc):
        a[i]=nc
        break
b=''.join(a)
print(b)
