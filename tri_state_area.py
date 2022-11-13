mod=987654319
def find(a,x):
    while 1:
        if a[x]<0:
            return x
        else:
            x=a[x]
def power(a,n):
    if(n==1):
        return a
    if n==0:
        return 1
    b=power(a,n//2)%mod
    if(n%2==0):
        return (b*b)
    else:
        return (b*b*a)%mod
n,t= map(int,input().split())
arr=[]
 
for j in range(n-1):
   x,y,c= map(int,input().split())
   arr.append([c,x,y])
arr.sort()
t=t+2
p=1
f=-1
a=[-1]*(n+1)
for j in arr:
    f=max(f,j[0])
    v=max(1,t-j[0])
    p1=find(a,j[1])
    p2=find(a,j[2])
    p=(p*power(v,(a[p1]*a[p2]-1))%mod)%mod
    a[p1]+=a[p2]
    a[p2]=p1
if(t<f):
    p=0
print(p%mod)
