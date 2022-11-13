import math,sys,bisect,heapq,os
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache

pr = lambda x:	x
def input(): return sys.stdin.readline().rstrip('\r\n')
aj = lambda: list(map(int, input().split()))
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])
 
def solve():
 
	def merge(a,b):
		new = [0,0,0]
		new[0] = a[0] + b[0]
		new[1] = max(a[1],b[1])
		new[2] = a[2] + b[2]
		return new
 
	def update(seg,n,a,b):
		a+=n
		seg[a] = [b,b,b%2]
		while a>1:
			a >>= 1
			seg[a] = merge(seg[2*a],seg[2*a + 1])
 
	def query(seg,n,ntrl,l,r):
	    r+=1;l+=n;r+=n
	    tot = ntrl
	    while l<r:
	        if l&1:
	            tot = merge(tot,seg[l]);l += 1
	        if r&1:
	            r-=1;tot = merge(tot,seg[r])
	        l = l//2;r = r//2
	    return tot
 
	def construct(A,ntrl):
		n = len(A)
		seg = [ntrl]*(2*n)
		for i in range(n):
			seg[n+i] = [A[i],A[i],A[i]%2]
		for i in range(n-1,0,-1):
			seg[i] = merge(seg[2*i],seg[2*i + 1])
		return seg
 
 
	ntrl= [0,0,0] 
	n,q = aj()
	A = aj()
	seg = construct(A,ntrl)

	for i in range(q):
		a,b,c = aj()
		if a == 2:
			b-=1;c-=1
			x,y,z = query(seg,n,ntrl,b,c)
			steps = 0
			ele = c-b + 1
			mxsum = ele*y
			if y % 2:
				even = ele - z
				steps += even
				dif = mxsum - x
				dif -= even
				steps += dif//2
			else:
				steps += z
				dif = mxsum - x
				dif -= z
				steps += dif//2
			print(steps)
		else:
			update(seg,n,b-1,c)
 
try:
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')
	from aj import *
except:
	pass
 
solve()
