def cubic_root(x, e=0.00001):
    if x==0:
        return 0
    
    c=x
    g=c
    g=g-(g**3-c)/(3*c*c)
    while True:
        diff=g**3-c
        if abs(diff)<=e:
            return g
        else:
            g=g-(g**3-c)/(3*c*c)
            
x=float(input())
#输入
print(cubic_root(x))