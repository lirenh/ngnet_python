class Digraph:
    """Directed Graph"""
    def __init__(self, num):
        """
        Initialize an empty directed graph
        Arguments:
        num -- number of vertices
        """
        self.graph = {}
        for i in range(num):
            self.graph[i] = []
        self.V, self.E = num, 0  #vertices, edges

    def add_edge(self, v1, v2):
        """edge: a pair of vertices, v1->v2"""
        self.graph[v1].append(v2)
        self.E += 1

    def adj(self, v):
        """Return adjacent vertices"""
        return self.graph[v]

marked = []

def descendants(G, synsets):
    """
    Return all the vertices reachable from the source vertices
    Arguments:
    G -- a Digraph
    g -- a set of synset IDs
    """
    global marked
    des = []
    marked = [False] * G.V
    diDFS(G, synsets)
    for i in range(G.V):
        if marked[i]:
            des.append(i)
    return des

def diDFS(G, vertices):
    """
    Computes the vertices in G that are connected to any of the source vertices.
    Arguments:
    G -- a Digraph
    vertices -- a set of vertices
    """
    for v in vertices:
        if not marked[v]:
            dfs(G, v)

def dfs(G, v):
    """helper function"""
    global marked
    #print("am", v, len(marked))
    marked[v] = True
    for av in G.adj(v):
        if not marked[av]:
            dfs(G, av)
