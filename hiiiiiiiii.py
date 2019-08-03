x=input()
l1=list(map(int,input().split()))
max=0
i=0
while(i<len(l1)-1):
    count=0
    while(i<len(l1)-1 and l1[i]<l1[i+1]):
        count+=1
        i+=1
    if(count>max):
        max=count
    i+=1
print(max+1)
