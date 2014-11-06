# Problem 82: path sum: 3 ways
# BFS with modification on stopping condition

from collections import deque

G = """
131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331
"""

G = None
with open("p082_matrix.txt") as f:
    G = f.read()

mapped = None
D = 80

class Node(object):
    def __init__(self, val, coord):
        self.val = val
        self.x, self.y = coord
        self.dist = float("inf")

    @property
    def coord(self):
        return (self.x, self.y)

    def __repr__(self):
        return "(%s,%s)@(%s,%s)"\
                % (self.val,self.dist,self.x,self.y)


def bfs(start_nodes):


    min_sum = float("inf")
    while start_nodes:
        local_min = float("inf")

        dq = deque()
        dq.append(start_nodes.pop(0))

        while dq:
            node = dq.popleft()

            if node.coord[0] == D-1:
                local_min = min(node.dist, local_min)
                min_sum = min(local_min, min_sum)

            right = mapped[(min(node.x+1, D-1), node.y)]
            up = down = None
            if node.coord[0] not in [0, D-1]:
                up = mapped[(node.x, max(node.y-1, 0))]
                down = mapped[(node.x, min(node.y+1, D-1))]

            for adj in [right, up, down]:
                if adj:
                    if adj.dist == float('inf') or\
                            adj.val+node.dist < adj.dist:
                        adj.dist = adj.val + node.dist
                        dq.append(adj)

    return min_sum


graph = [[Node(int(val), (col, row)) for col, val in\
        enumerate(row_val.split(","))] for row, row_val in\
        enumerate(G.split())]
graph = [node for row in graph for node in row]
mapped = dict([(node.coord, node) for node in graph])

start_nodes = []
for row in xrange(D):
    node = mapped[(0, row)]
    node.dist = node.val
    start_nodes.append(node)

from time import time, sleep

start = time()
print bfs(start_nodes)
print "DONE", time()-start
