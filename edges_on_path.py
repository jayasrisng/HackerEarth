from collections import defaultdict 
 
class Graph: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = defaultdict(list) 
 
	def addEdge(self, u, v): 
		self.graph[u].append(v)  
 
	def printAllPathsUtil(self, u, d, visited, path): 
		visited[u]= True
		path.append(u) 
 
		if u == d: 
			Ans.append(path.copy())
		else: 
			for i in self.graph[u]: 
				if visited[i]== False: 
					self.printAllPathsUtil(i, d, visited, path) 
		path.pop() 
		visited[u]= False
 
	def printAllPaths(self, s, d): 
		visited =[False]*(self.V) 
		path = [] 
		self.printAllPathsUtil(s, d, visited, path) 
 
Ans = []
n,m = map(int,input().split())
a,b = map(int,input().split())
g = Graph(n+1)
for i in range(m):
    u,v = map(int,input().split())
    g.addEdge(u,v)
    g.addEdge(v,u)
 
g.printAllPaths(a, b) 
if len(Ans) == 1:
    print(len(Ans[0])-1)
else:
    p,q = 0,0 
    k = min(len(Ans[0]),len(Ans[1]))
    for i in range(k):
        if Ans[0][i] == Ans[1][i]:
            p += 1
    Ans = [Ans[0][::-1],Ans[1][::-1]]
    for i in range(k):
        if Ans[0][i] == Ans[1][i]:
            q += 1
    print(p+q-2)
