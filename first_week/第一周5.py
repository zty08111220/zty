x=input()
y=input()
z=input()
if x>=y:
    if y>=z:
        print(z,y,x)
    elif z>=x:
        print(y,x,z)
    else:
        print(y,z,x)
else:
    if z>=y:
        print(x,y,z)
    elif x>=z:
        print(z,x,y)
    else:
        print(x,z,y)