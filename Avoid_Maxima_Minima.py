def build(n):
    a = [[0]]
    while len(a[-1]) < n:
        a.append(a[-1] + a[-1])
    return a
 
def update(a, i, v):
    i -= 1
    row = len(a) - 1
    while row >= 0:
        if a[row][i] >= v:
            return
        a[row][i] = v
        row -= 1
        i >>= 1
 
def query(a, l, r):
    l -= 1
    r -= 1
    row = len(a) - 1
    ans = 0
    while l <= r:
        if l&1:
            if ans < a[row][l]: ans = a[row][l]
            l += 1
        if not (r&1):
            if ans < a[row][r]: ans = a[row][r]
            r -= 1
        l >>= 1
        r >>= 1
        row -= 1
    return ans
 
 
def solve(a, n):
    inc = build(n)
    dec = build(n)
    act = build(n)
 
    for v in a:
        imx = query(inc, 1, v)
        amx = query(act, 1, v)
        ival = max(imx, dec[-1][v-1], amx) + 1
 
        dmx = query(dec, v, n)
        amx = query(act, v, n)
        dval = max(dmx, inc[-1][v-1], amx) + 1
 
        update(act, v, max(inc[-1][v-1], dec[-1][v-1]))
        update(inc, v, ival)
        update(dec, v, dval)
 
    return inc[0][0] if inc[0][0] > dec[0][0] else dec[0][0]
 
 
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a, n))
