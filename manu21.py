a1,b1=map(int,input().split())
for i in range(a1+1,b1):
    s=0
    a=i
    while(a>0):
        c=a%10
        s+=c**3
        a//=10
    if(i==s):
            print(i,end=" ")
    
