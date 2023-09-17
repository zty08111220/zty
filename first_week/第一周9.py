num=int(input())
L=[]
for i in range (1,num+1):
    L.append(int(input()))
#for
reverse_list1=[]
for i in range(len(L) - 1, -1, -1):
    reverse_list1.append(L[i])
print(reverse_list1)
#while
reverse_list2=[]
i=len(L)-1
while i>=0:
    reverse_list2.append(L[i])
    i-=1
print(reverse_list2)