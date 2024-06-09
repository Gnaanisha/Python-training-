str1=input()
#f=0
a = ""
for i in range(len(str1)):
    b=str1[i]
    fl=0
    for i in range(i):
        if str1[i] ==b:
            fl=1
            break
    if not fl:
        a=a+b
print(a)
