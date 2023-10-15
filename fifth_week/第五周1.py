import sys
a=int(input())
i=2
while i<=a**0.5:
    if a%i==0:
        print("非质数")
        sys.exit()
    i=i+1
print("质数")
    