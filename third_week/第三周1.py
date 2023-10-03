x=float(input())
i=-1
ans=0
while i>=-15:
    if x-2**i>=0:
        ans=ans+10**i
        x=x-2**i
    i=i-1
print(ans)