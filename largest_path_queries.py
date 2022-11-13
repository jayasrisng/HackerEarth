from sys import stdin
from collections import deque, defaultdict
 
class Graph:
    def __init__ (self, q):
        q += 1
        self.logn = 16
        self.vertices = 1
        self.adj = defaultdict (list)
        self.dis = [0, 0]
        self.par = [0, 0]
        self.dia = 0
        self.d1 = 1  
        self.d2 = 1 
        self.p = [[0] * 17 for i in range (q)]
    def addEdge (self, u, v):  # v is new
        self.adj [u].append (v)
        self.adj [v].append (u)
        self.vertices += 1
        self.dis.append (self.dis [u] + 1)
        self.par.append (u) 
        self.p [self.vertices][0] = u
        for j in range (1, self.logn + 1):
            self.p [self.vertices][j] = self.p [self.p [self.vertices][j - 1]][j - 1]
        if self.par [v] == self.d1:
            self.dia += 1
            self.d1 = v
            return
        elif self.par [v] == self.d2:
            self.dia += 1
            self.d2 = v
            return
        d = self.dis [v] + self.dis [self.d1] - 2 * self.dis [self.lca (v, self.d1)]
        if d > self.dia:
            self.dia = d
            self.d2 = v
        else:
            d = self.dis [v] + self.dis [self.d2] - 2 * self.dis [self.lca (v, self.d2)]
            if d > self.dia:
                self.dia = d
                self.d1 = v
    def lca1 (self, u, v):
        ul = deque ([u]); vl = deque ([v])
        while self.par [ul [0]]: ul.appendleft (self.par [ul [0]])
        while self.par [vl [0]]: vl.appendleft (self.par [vl [0]])
        lim = len (ul) if len (ul) < len (vl) else len (vl)
        res = 0
        for i in range (lim):
            if ul [i] == vl [i]: res = ul [i]
            else: break
        return res
    def lca (self, u, v): # faster
        if self.dis [u] > self.dis [v]: u, v = v, u
        d = self.dis [v] - self.dis [u]
        for i in range (self.logn, -1, -1):
            if (d >> i) & 1: v = self.p [v][i]
        if u == v: return u
        for i in range (self.logn, -1, -1):
            if self.p [u][i] != self.p [v][i]:
                u = self.p [u][i]
                v = self.p [v][i]
        return self.p [u][0]
 
def main ():
    read = stdin.readline
    t = int (read ())
    for t_ in range (t):
        q = int (read ())
        g = Graph (q)
        lx = 0; ld1 = 0; ld2 = 0
        lca_disd = dict ()
        ql = []
        for q_ in range (q):
            k, x = map (int, read ().split ())
            ql.append ((k, x))
        for k, x in ql:
            if k == 1:
                g.addEdge (x, g.vertices + 1)
            elif (x, g.d1, g.d2) in lca_disd:
                print (lca_disd [(x, g.d1, g.d2)])
            else:
                lca_node = g.lca (g.d1, x)
                lca_dis = g.dis [x] + g.dis [g.d1] - 2 * g.dis [lca_node]
                lca_node = g.lca (g.d2, x)
                lca_dis2 = g.dis [x] + g.dis [g.d2] - 2 * g.dis [lca_node]
                if lca_dis2 > lca_dis: lca_dis = lca_dis2
                lca_disd [(x, g.d1, g.d2)] = lca_dis
                print (lca_dis)
 
if __name__ == "__main__": main ()
