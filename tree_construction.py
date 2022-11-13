m = 1000000007
tot = 1
n = int(input())
g = [[]for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u] += [v]
    g[v] += [u]

def dfs(u = 0, p = -1):
    global tot
    res = 1
    for v in g[u]:
        if v != p:
            res = (res * dfs(v, u)) % m
    tot += res
    return res + 1
dfs()
print(tot % m)
