#随机投点法
import math
import random
s=0
for i in range (1,1000000):
    x=random.uniform(0,2)
    y=random.uniform(0,2)
    if ((x-1)**2+(y-1)**2)**0.5<=1:
        s=s+1
x=s/1000000
pi=x*4
print(format(pi,'.10f'))

#BBP公式
pi=0
for i in range (0,1000):
    pi+=1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print(format(pi,'.10f'))

#梅钦公式
pi=4*(4*math.atan(1/5)-math.atan(1/239))
print(format(pi,'.10f'))