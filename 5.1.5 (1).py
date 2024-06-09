n=int(input())
b=[]
for i in range(0,n):
    a=float(input())
    b.append(a)

mean = 0
for x in b:
    mean += x
mean /= n
variance = 0
for x in b:
    variance += (x - mean) ** 2
variance /=n
std_deviation = variance ** 0.5

print("Mean:{:.2f}".format(mean))
print("Variance:{:.2f}".format(variance))
print("Standard Deviation:{:.2f}".format(std_deviation))   
            


