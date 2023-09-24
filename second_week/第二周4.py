def cubic_root(x, e=0.00001):
    if x==0:
        return 0
    
    low=0
    high=x
    while True:
        mid=(low+high)/2
        diff=mid**2-x
        if abs(diff)<=e:
            return mid
        elif diff<0:
            low=mid
        else:
            high=mid
            
x=float(input())
#输入2
print(cubic_root(x))