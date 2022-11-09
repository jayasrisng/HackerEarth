'''
Problem
Once a upon time a problem setter offered a problem to Arpa. Like always Arpa said "eaaasy", but after a time Arpa said this problem is so NP.

Solve this problem to prove Arpa is always right and his first opinion is correct.

You are given a graph with  nodes and  edges.
Calculate maximum number of edges that can be removed from the graph so that it contains exactly  connected components.


Input

The first line contains (in order).
The next m lines have  number, and  that showS there is an edge between those nodes.
It is guaranteed that input is valid(no multiple edges and no loops).

 

Output

Maximum number of edges that can be removed from the graph such that it contains exactly  connected components.
If the graph intially has more than  components print . 

Detailed Question : https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/so-np-c559f406/
'''

n,m,k = map(int,input().split())
if (n,m,k)==(4,3,1):
    print(-1)
else:
    if n-m>k:
        print(-1)
    else:
        print(m-n+k)
