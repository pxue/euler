# Problem 81: Path sum: two ways
# BFS with modification to check already traversed
#   path to obtain the shortest one

G = None
with open("p081_matrix.txt") as f:
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
                % (self.val,self.dist,self.x, self.y)

def bfs(graph):

    start = graph[0]
    start.dist = start.val
    
    tmp_queue = [start]
    while tmp_queue:
        node = tmp_queue.pop(0)

        if (79,79) == node.coord:
            break

        right = mapped[(min(node.x+1, D-1), node.y)]
        down = mapped[(node.x, min(node.y+1, D-1))]

        for adj in [right, down]:
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
