from sys import stdin
 
class my:
    __slots__ = "cntPref", "cntSuff", "cntAll", "val"
    def __init__ (self):
        self.cntPref = 0
        self.cntSuff = 0
        self.cntAll = 1
        self.val = 1
 
def main ():
    read = stdin.readline
    mod = 10 ** 9 + 7
    n, m = map (int, read ().split ())
    n1 = n + 1
    p = [0] + list (map (int, read ().split ()))
    f = [0] * n1  # factorial modulus
    rf = [0] * n1
    pos = [0] * n1
    mx = max (n, m) + 1
    q = [[] for i in range (mx)]
    for i in range (1, n1):
        pos [p [i]] = i
    t = [my () for i in range (4 * n)]
    answer = [0] * mx
    def fakmod (n):
        r = 1
        for i in range (1, n1):
            r = r * i % mod
            f [i] = r
            rf [i] = pow (r, mod - 2, mod)
    fakmod (n)
    for ix in range (1, m + 1):
        l, r, x = map (int, read ().split ())
        q [x].append (((l, r), ix))
 
    def combine (a, b):
        c = my ()
        c.cntAll = a.cntAll + b.cntAll
        if b.cntPref and a.cntSuff:
            if a.cntAll == a.cntSuff and b.cntAll == b.cntPref:
                c.cntPref = c.cntAll
                c.cntSuff = c.cntAll
            elif a.cntAll == a.cntSuff:
                c.cntPref = a.cntAll + b.cntPref
                c.cntSuff = b.cntSuff
            elif b.cntAll == b.cntPref:
                c.cntPref = a.cntPref
                c.cntSuff = b.cntAll + a.cntSuff
            else:
                c.cntPref = a.cntPref
                c.cntSuff = b.cntSuff
            c.val = a.val * b.val % mod * rf [a.cntSuff] % mod * rf [b.cntPref] % mod * f [a.cntSuff + b.cntPref] % mod
        else:
            c.cntPref = a.cntPref
            c.cntSuff = b.cntSuff
            c.val = a.val * b.val % mod
        return c
 
    def upd (v, tl, tr, pos):
        if tl > pos or tr < pos: return
        if tl == tr:
            t[v].cntPref, t[v].cntSuff, t[v].cntAll, t[v].val = 1, 1, 1, 1
            return
        tm = (tl + tr) >> 1
        L = v << 1
        R = L | 1
        upd (L, tl, tm, pos)
        upd (R, tm + 1, tr, pos)
        t [v] = combine (t [L], t [R])
 
    def get (v, tl, tr, l, r):
        if tl >= l and tr <= r: return t [v]
        tm = (tl + tr) >> 1
        L = v << 1
        R = L | 1
        if r <= tm: return get (L, tl, tm, l, r)
        if l > tm: return get (R, tm + 1, tr, l, r)
        a1 = get (L, tl, tm, l, r)
        a2 = get (R, tm + 1, tr, l, r)
        a3 = combine (a1, a2)
        return a3
    for i in range (1, n1):
        upd (1, 1, n, pos [i])
        for j in range (len (q [i])):
            answer [q [i][j][1]] = get (1, 1, n, q [i][j][0][0], q [i][j][0][1]).val
    for i in range (1, m + 1):
        print (answer [i])
 
if __name__ == "__main__": main ()
