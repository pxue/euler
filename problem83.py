# Problem 83: Path sum: four ways
# BFS with modification to check already traversed
#   path to obtain the shortest one
#   modified stopping condition from problem81

G = None
with open("p083_matrix.txt") as f:
    G = f.read()
#G = """
#131,673,234,103,18
#201,96,342,965,150
#630,803,746,422,111
#537,699,497,121,956
#805,732,524,37,331
#"""

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
                % (self.val,self.dist,self.x, self.y)

def bfs(graph):

    start = graph[0]
    start.dist = start.val
    
    tmp_queue = [start]
    while tmp_queue:
        node = tmp_queue.pop(0)

        if (D-1,D-1) == node.coord and len(tmp_queue) == 0:
            print node

        left = mapped[(max(node.x-1, 0), node.y)]
        right = mapped[(min(node.x+1, D-1), node.y)]
        up = mapped[(node.x, max(node.y-1, 0))]
        down = mapped[(node.x, min(node.y+1, D-1))]

        for adj in [left, right, up, down]:
            if adj != node:
                if adj.dist == float('inf') or\
                        adj.val+node.dist < adj.dist:
                    adj.dist = adj.val + node.dist
                    tmp_queue.append(adj)


graph = [[Node(int(val), (col, row)) for col, val in\
        enumerate(row_val.split(","))] for row, row_val in\
        enumerate(G.split())]
graph = [node for row in graph for node in row]
mapped = dict([(node.coord, node) for node in graph])

bfs(graph)
