from collections import defaultdict, deque
import math, sys
 
def bfs(edges, source, t):
    visited[source] = t
    queue = deque([(source, 1)])
 
    while queue:        
        curr_node, curr_dist = queue.popleft()
        for v in edges[curr_node]:
            if visited[v] != t:
                visited[v] = t
                queue.append((v, curr_dist+1))
 
    return curr_node, curr_dist
 
n, m, f = map(int, sys.stdin.readline().split())
 
edges = defaultdict(set)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    edges[x].add(y)
    edges[y].add(x)
 
visited = {x:0 for x in edges}
 
max_dist = 1
 
for node in edges:
 
    if visited[node] > 0:
        continue
 
    last_node, _ = bfs(edges, node, 1)
    _, dist = bfs(edges, last_node, 2)
    max_dist = max(max_dist, dist)
 
print( math.ceil( max_dist/f) )
