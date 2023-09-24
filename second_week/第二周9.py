import numpy as np
import math
import random
sum=0
for i in range (1,100000):
    x=random.uniform(2,3)
    y=4*x*math.sin(x)+x*x
    sum=sum+y
print(sum/100000)