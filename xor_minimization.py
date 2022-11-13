n = int(input())
l = [int(x) for x in input().split()]
s = sum(l)
dp = [1] + [0] * s
for x in l:
	for i in range(s, -1, -1):
		if dp[i]:
			dp[i+x] = (dp[i+x] + dp[i])  % 1000000007
 
tree = []
def add(tree, num, count):
	mask = 1<<17
	while mask:
		index = bool(num & mask)
		if not tree:
			tree.extend([[], []])
		tree = tree[index]
		mask >>= 1
	tree.append((num, count))
 
def search(tree, num):
	mask = 1<<17
	while mask:
		index = bool(num & mask)
		if tree[index]:
			tree = tree[index]
		else:
			tree = tree[1 - index]
		mask >>= 1
	return "{} {}".format(*tree[0])
 
for i, x in enumerate(dp[1:]):
	if x:
		add(tree, i+1, x)
 
q = int(input())
import sys
for qs in sys.stdin:
	a = int(qs) & ((1<<18) - 1)
	print(search(tree, a))
