import random
n=int(input())
a=[1]*n
b=[1]*n
for i in range (0,n):
    a[i]=random.uniform(1,10)
for i in range (0,n):
    sum=1
    for j in range (0,i):
        sum=sum*a[j]
    for j in range (i+1,n):
        sum=sum*a[j]
    b[i]=sum
for i in range (0,n):
    print(b[i])
#n自己输入 数组a内元素为1到10之间的随机浮点数