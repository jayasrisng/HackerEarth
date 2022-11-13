from queue import *
n,m=list(map(int,input().rstrip().split()))
graph=[[] for i in range(0,n+1)]
dis=[1e9]*(n+1)
dis[1]=0
q=Queue()
def update(v):
    for i in graph[v]:
        if dis[i]>dis[v]+1:
            dis[i]=dis[v]+1
            update(i)                     
while(m):
    m-=1
    temp=list(map(int,input().rstrip().split()))
    if(temp[0]==1):
        if (dis[temp[1]]==1e9):
            print(-1)
        else:
            print(dis[temp[1]])
    else:
        graph[temp[1]].append(temp[2])
        if(dis[temp[2]]>dis[temp[1]]+1):
            dis[temp[2]]=dis[temp[1]]+1
            update(temp[2])
