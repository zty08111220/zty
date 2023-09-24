def cubic_root1(x, e=0.00001):
    if x==0:
        return 0
    
    c=x
    g=c/2
    while True:
        diff=g**2-c
        if abs(diff)<=e:
            return g
        else:
            g=(g+c/g)/2
#g=c/2          
def cubic_root2(x, e=0.00001):
    if x==0:
        return 0
    
    c=x
    g=c
    while True:
        diff=g**2-c
        if abs(diff)<=e:
            return g
        else:
            g=(g+c/g)/2
#g=c
def cubic_root3(x, e=0.00001):
    if x==0:
        return 0
    
    c=x
    g=c/4
    while True:
        diff=g**2-c
        if abs(diff)<=e:
            return g
        else:
            g=(g+c/g)/2
#g=c/4   
x=float(input())
#输入
print(cubic_root1(x))
print(cubic_root2(x))
print(cubic_root3(x))

#结论：对结果有影响的。大部分情况下是不一样的，存在其中两种相同的概率。具体精度经过多次尝试，每种均有概率较其他更为精确。