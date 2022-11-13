from collections import defaultdict
import sys
  
sys.setrecursionlimit(100000000)
 
 
def inp(): return int(input())
def inps(): return input().strip()
 
 
def jn(x, l): return x.join(map(str, l))
def strl(): return list(input().strip())
 
 
def mul(): return map(int, input().strip().split())
def mulf(): return map(float, input().strip().split())
def seq(): return list(map(int, input().strip().split()))
 
 
def solve():
 
    k, q = seq()
 
    def get_path(x):
        ans = [x]
        while x != 1:
            x = x // k
            ans.append(x)
        return ans
 
    def get_lca(u, v):
        path1, path2 = get_path(u), get_path(v)
        while path1 and path2 and path1[-1] == path2[-1]:
            path1.pop()
            path2.pop()
        return path1, path2
 
    wd = defaultdict(lambda: 1)
 
    for _ in range(q):
        data = seq()
 
        if data[0] == 1:
            _, u, v = data
            path1, path2 = get_lca(u, v)
            w = 0
            for x in path1:
                w += wd[x]
            for x in path2:
                w += wd[x]
            print(w)
        else:
            _, u, v, w = data
            path1, path2 = get_lca(u, v)
            for x in path1:
                wd[x] += w
            for x in path2:
                wd[x] += w
 
solve()
