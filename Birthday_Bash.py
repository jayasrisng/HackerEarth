import bisect
#from sortedcontainers import SortedList, SortedSet, SortedDict
t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    s=str(input())
    s1=list(s)
    idx=[]
    d={}
    for j in range(q):
        a,b=map(int,input().split())
        if(a==1):
            b=min(b,len(s)-1-b)
            if(b in d):
                d.pop(b)
                idx.remove(b)
            else:
                d[b]=0
                bisect.insort(idx,b)
        else:
            f=min(b,len(s)-1-b)
            itr=bisect.bisect(idx,f)
            up=b
            if(itr%2==1):
                up=len(s)-1-b
            if(s1[up]=="z"):
                s1[up]="a"
            else:
                s1[up]=chr(ord(s1[up])+1)
    fin=""
    flg=[0]*len(s)
    cur=0
    for i in range(len(s)//2):
        if(i in d):
            cur+=1
        if(cur%2==0):
            fin+=s1[i]
            flg[i]=1
        else:
            fin+=s1[len(s)-1-i]
            flg[len(s)-1-i]=1
    for i in range(len(s)//2,len(s)):
        if(flg[i]==0):
            fin+=s1[i]
        else:
            fin+=s1[len(s)-1-i]
    print(fin)   
