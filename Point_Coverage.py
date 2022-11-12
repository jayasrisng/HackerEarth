#!/usr/bin/python3
from sys import stdin, stdout
#from collections import namedtuple
 
def update (BIT, n, idx, val):
    while idx <= n:
        BIT [idx] += val
        idx += idx & -idx
        
def query (BIT, idx):
    ans = 0
    while idx:
        ans += BIT [idx]
        idx -= idx & -idx
    return ans
 
def solveQuery (arr, n, QueryL, QueryR, QueryX, q):
    a = []  
    for i in range (1, n):   
        mn = arr [i]; mx = arr [i + 1]
        if mn > mx: mn, mx = mx, mn
        a.append ((mn, 1, i))  
    for i in range (1, q + 1):  
        a.append ((QueryX [i], 2, i))
    a = sorted (a , key = lambda k: (k [0], k [1]))
    BIT = [0] * (n + 1)   
    ans = [0] * (q + 1)   
    for nd in a:  
        if nd [1] == 1: update (BIT, n, nd [2], 1)
        elif nd [1] == 2:
            ans [nd [2]] = query (BIT, QueryR [nd [2]])\
                    - query (BIT, QueryL [nd [2]] - 1)
        else: update (BIT, n, nd [2], -1)
    return ans
 
def main ():
    read = stdin.readline
    write = stdout.write
    n, q = map (int, read ().split ())
    a = [0] + list (map (int, read ().split ()))
    QueryL = [0]; QueryR = [0]; QueryX = [0]
    for q_ in range (q):
        l, r, x = map (int, read ().split ())
        QueryL.append (l)
        QueryR.append (r)
        QueryX.append (x)
    ans = solveQuery (a, n, QueryL, QueryR, QueryX, q)
    for i in range (1, q + 1):
        write (str (ans [i]) + '\n')
 
if __name__ == "__main__": main ()
