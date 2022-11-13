from sys import stdin
from math import gcd
  
def dfs(adj):
    n = len(adj)
    visited = [False] * n
    pointer = [0] * n
    nodes = []
    for x in range(n):
        if not visited[x]:
            s = [x]
            visited[x] = True
            while s:
                y = s[-1]
                any_more = False
                for i in range(pointer[y], len(adj[y])):
                    z = adj[y][i]
                    pointer[y] += 1
                    if not visited[z]:
                        s.append(z)
                        visited[z] = True
                        any_more = True
                        break
                if not any_more:
                    nodes.append(y)
                    s.pop()
    return nodes
 
 
def reverse_adj(adj):
    n = len(adj)
    rev_adj = [[] for _ in range(n)]
    for x in range(n):
        for y in adj[x]:
            rev_adj[y].append(x)
    return rev_adj
 
 
def strongly_connected_components(rev_adj, nodes):
    n = len(nodes)
    visited = [False] * n
    pointer = [0] * n
    comp_num = [-1] * n
    condensed_adj = []
    reachable = [1] * n
    i = 0
    while nodes:
        x = nodes[-1]
        if visited[x]:
            nodes.pop()
            continue
        visited[x] = True
        s = [x]
        comp_num[x] = i
        condensed_adj.append([])
        while s:
            y = s[-1]
            any_more = False
            for j in range(pointer[y], len(rev_adj[y])):
                z = rev_adj[y][j]
                pointer[y] += 1
                if not visited[z]:
                    s.append(z)
                    comp_num[z] = i
                    visited[z] = True
                    any_more = True
                    break
                elif comp_num[z] == i:
                    continue
                else:
                    condensed_adj[comp_num[z]].append(i)
            if not any_more:
                s.pop()
        i += 1
    return comp_num, condensed_adj
 
 
def topological_sort(adj):
    n = len(adj)
    nodes = []
    visited = [False] * n
    pointer = [0] * n
    for x in range(n):
        if not visited[x]:
            s = [x]
            visited[x] = True
            while s:
                y = s[-1]
                any_more = False
                for i in range(pointer[y], len(adj[y])):
                    z = adj[y][i]
                    pointer[y] += 1
                    if not visited[z]:
                        s.append(z)
                        visited[z] = True
                        any_more = True
                        break
                if not any_more:
                    s.pop()
                    nodes.append(y)
    top_sort = []
    while nodes:
        x = nodes.pop()
        top_sort.append(x)
    parents = [[] for _ in range(n)]
    for x in range(n):
        for y in adj[x]:
            parents[y].append(x)
    return top_sort, parents
 
 
def get_answer(adj, costs):
    nodes = dfs(adj)
    rev_adj = reverse_adj(adj)
    comp_num, condensed_adj = strongly_connected_components(rev_adj, nodes)
    n_full = len(adj)
    n_condensed = len(condensed_adj)
    condensed_costs = [None] * n_condensed
    for x in range(n_full):
        if condensed_costs[comp_num[x]] is None:
            condensed_costs[comp_num[x]] = costs[x]
        else:
            condensed_costs[comp_num[x]] = gcd(condensed_costs[comp_num[x]], costs[x])
    answer = float('inf')
    answers = [None] * n_condensed
    top_sort, parents = topological_sort(condensed_adj)
    for x in top_sort:
        answers[x] = condensed_costs[x]
        for y in parents[x]:
            answers[x] = min(answers[x], gcd(answers[y], condensed_costs[x]))
        if answers[x] < answer:
            answer = answers[x]
    return answer
 
 
def solve():
    n, m = list(map(int, stdin.readline().strip().split()))
    costs = list(map(int, stdin.readline().strip().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x, y = list(map(int, stdin.readline().strip().split()))
        adj[x - 1].append(y - 1)
    print(get_answer(adj, costs))
 
 
solve()
