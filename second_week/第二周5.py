def cubic_root(x, e=0.00001):
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
            
x=float(input())
#输入
print(cubic_root(x))