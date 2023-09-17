import sys
x=input()
tep='\0'
for i in x:
    if tep==i:
        print("yes")
        sys.exit()
    tep=i
print("no")