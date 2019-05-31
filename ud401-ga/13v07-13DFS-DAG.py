from collections import defaultdict

def edges_to_adjlist(edges):
    adjlist = defaultdict(list)
    for s,t in edges:
        adjlist[s].append(t)
    return adjlist

def classic_dfs(graph, start):
    visited = set()
    def dfs(graph, v):
        if v not in visited:
            visited.add(v)
            for t in graph[v]:
                dfs(graph, t)
    dfs(graph, start)
    return visited

def dfs1(graph, start):
    visited = set()
    clock = 1
    pre, post = {}, {}
    def setclock(obj, z):
        nonlocal clock
        obj[z]  = clock
        clock += 1
    def explore(z):
        setclock(pre, z)
        visited.add(z)
        for t in graph[z]:
            if t not in visited:
                explore(t)
        setclock(post, z)
    for v in graph:
        if v not in visited:
            explore(v)
    return pre, post



if __name__ == '__main__':
    edges = [
        ('A', 'D'),
        ('B', 'A'),('B', 'E'),('B', 'C'),
        ('C', 'F'),
        ('D', 'E'),('D', 'H'),('D', 'G'),
        ('E', 'A'),('E', 'G'),
        ('F', 'B'),('F', 'H'),
        ('H', 'G'),
    ]
    print(edges_to_adjlist(edges))
    adjlist0 = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3], 5: [6], 6: [5]}
    adjlist1 = {
        'A': ['D'],
        'B': ['A', 'C', 'E'],
        'C': ['F'],
        'D': ['E', 'H', 'G'],
        'E': ['G', 'A'],
        'F': ['B', 'H'],
        'H': ['G'],
        'G': [],
    }
    print(dfs1(adjlist0, 1))
    print(dfs1(adjlist1, 'B'))