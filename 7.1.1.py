str1= input()
f= {}
for i in str1:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
for i in f:
    print(f"{i} = {f[i]}")
