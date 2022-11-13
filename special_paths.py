from sys import stdin
from heapq import heappush, heappop
 
def main ():
    MAX = 10 ** 10
    read = stdin.readline
    n, m = (int (x) for x in read ().split ())
    ed = [[] for i in range (n + 1)]
    for m_ in range (m):
        u, v = (int (x) for x in read ().split ())
        ed [u].append (v)
        ed [v].append (u)
    nv = [0] + [int (x) for x in read ().split ()]
    st, e = (int (x) for x in read ().split ())
    vstd = [False] * (n + 1)
    q = [(0, st)]
    # based on Dijkstra
    while q:
        cost, nd = heappop (q)
        if vstd [nd]: continue
        if nd == e: 
            print (cost)
            break
        vstd [nd] = True
        for adj in ed [nd]:
            if vstd [adj]: continue
            heappush (q, (max (cost, abs (nv [adj] - nv [nd])), adj))
 
if __name__ == "__main__": main ()
