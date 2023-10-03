import sys
x=int(input())
y=int(input())
if x>=y:
    i=x
    while i>=0:
        if x%i==0 and y%i==0:
            print(i)
            sys.exit()
        i=i-1
else:
    i=y
    while i>=0:
        if x%i==0 and y%i==0:
            print(i)
            sys.exit()
        i=i-1