import sys
from collections import deque
from collections import OrderedDict as dict 
 
INFINITE = 999999999999
 
global_edges = set()
def solve():
    r, c = list(map(int, sys.stdin.readline().split()))
    val = []
    indirect = []
    direct = []
    for array in [val, indirect, direct]:
        for row in range(r):
            array.append(list(map(int, sys.stdin.readline().split())))
    print(solve_single(val, indirect, direct, r, c))
 
def solve_single(val, indirect, direct, row, col):
    source = GraphNode('src')
    sink = GraphNode('sink')
 
    total_possible = 0
    nodes_p = []
    nodes_s = []
    for r in range(row):
        col_list_p = []
        col_list_s = []
        for c in range(col):
            col_list_p.append(GraphNode("({0}, {1})*".format(r, c)))
            col_list_s.append(GraphNode("({0}, {1})**".format(r, c)))
            total_possible += val[r][c]
        nodes_p.append(col_list_p)
        nodes_s.append(col_list_s)
 
    for r in range(row):
        for c in range(col):
            n1 = nodes_p[r][c]
            n2 = nodes_s[r][c]
            add_edge(n1, n2, val[r][c])
            if (r % 2) == (c % 2):
                add_edge(source, n1, direct[r][c])
                add_edge(n2, sink, indirect[r][c])
                for plus in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    x, y = plus
                    n_x = c + x
                    n_y = r + y
                    if n_x >= 0 and n_x < col and n_y >= 0 and n_y < row :
                        add_edge(n1, nodes_p[n_y][n_x], INFINITE)
                        add_edge(n2, nodes_s[n_y][n_x], INFINITE)
            else:
                add_edge(source, n1, indirect[r][c])
                add_edge(n2, sink, direct[r][c])
 
    while mod_bfs(source, sink):
        pass
 
    return total_possible - calculate_cut(source)
 
class GraphNode(object):
    def __init__(self, label):
        self.label = label
        self.connections = dict()
        self.residuals = dict()
 
    def __repr__(self):
        return self.label
 
class GraphEdge(object):
    def __init__(self, source, destination, direct_weight):
        self.source = source
        self.destination = destination
        self.direct_weight = direct_weight 
        self.orig_weight = direct_weight
        self.residual_weight = 0
    def __repr__(self):
        return "src: {0}, dest: {1}, dw: {2}, rw: {3}\n".format(self.source, self.destination, self.direct_weight, self.residual_weight)
 
def add_edge(source, destination, direct_weight):
    ge = GraphEdge(source, destination, direct_weight)
    source.connections[destination] = ge
    destination.residuals[source] = ge
    global_edges.add(ge)
    return ge
 
def mod_bfs(sourceNode, sinkNode):
    RESIDUAL = True
    DIRECT = False
 
    visited = set()
    visited.add(sourceNode)
    queue = deque()
    for element in sourceNode.connections:
        connection = sourceNode.connections[element]
        if connection.direct_weight > 0:
            queue.append((connection.destination, connection.direct_weight, [(sourceNode, DIRECT)]))
 
    while len(queue) > 0:
        node, weight, his = queue.popleft()
        history = list(his)
        if node == sinkNode:
            history.append((node, DIRECT))
            for index in range(len(history)-1):
                node, typed = history[index]
                next_node, next_typed = history[index + 1]
                if typed == RESIDUAL:
                    edge = node.residuals[next_node]
                    edge.residual_weight -= weight
                    edge.direct_weight += weight
                elif typed == DIRECT:
                    edge = node.connections[next_node]
                    edge.direct_weight -= weight
                    edge.residual_weight += weight
            return True
        else:
            for element in node.connections:
                connection = node.connections[element]
                if connection.direct_weight > 0 and connection.destination not in visited:
                    min_weight = weight if weight < connection.direct_weight else connection.direct_weight
                    new_history = list(history)
                    new_history.append((node, DIRECT))
                    queue.append((connection.destination, min_weight, new_history))
                    visited.add(connection.destination)
            for element in node.residuals:
                connection = node.residuals[element]
                if connection.residual_weight > 0 and connection.source not in visited:
                    min_weight = weight if weight < connection.residual_weight else connection.residual_weight
                    new_history = list(history)
                    new_history.append((node, RESIDUAL))
                    queue.append((connection.source, min_weight, new_history))
                    visited.add(connection.source)
    return False
 
def calculate_cut(source):
    cut = 0
    visited = set()
    queue = deque()
    queue.append(source)
    visited.add(source)
    while len(queue) > 0:
        node = queue.popleft()
        for element in node.connections:
            connection = node.connections[element]
            if connection.destination not in visited and connection.direct_weight > 0:
                visited.add(connection.destination)
                queue.append(connection.destination)
        for element in node.residuals:
            connection = node.residuals[element]
            if connection.source not in visited and connection.residual_weight > 0:
                visited.add(connection.source)
                queue.append(connection.source)
    for node in visited:
        for element in node.connections:
            if element not in visited:
                cut += node.connections[element].residual_weight
    return cut
 
solve()
