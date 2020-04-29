"""
APSP = all pair shortest path

Easy: run Bellman-Ford for all s in V
Running time: O(n^2 * m)

Now Floyd-Warshall O(n^3) time

for 0 ≤ i ≤ n and 0 ≤ s,t ≤ n:
    D(i,s,t) = length of shortest path from s to z
        using a subset of {0,...,i} as intermediate vertices

base case: D(0,s,t) = w(s,t)    if (s,t) in E
                    = inf       otherwise

"""

from math import inf

def extract_vertices(graph):
    vertices = set(graph.keys())
    for dest in graph.values():
        for v in dest.keys():
            vertices.add(v)
    return list(sorted(vertices))

def extract_reverse_graph(graph, vertices):
    reverse_graph = {v:set() for v in vertices}
    for src, dests in graph.items():
        for dest in dests:
            reverse_graph[dest].add(src)
    return reverse_graph

def floyd_warshall(graph):
    vertices = extract_vertices(graph)
    print(vertices)
    n = len(vertices)
    reverse_graph = extract_reverse_graph(graph, vertices)
    dist = {(s,t): inf for s in vertices for t in vertices if s != t}
    newdist = None
    for s in graph:
        for t, w in graph[s].items():
            dist[(s,t)] = w
    for i in vertices:
        newdist = dist.copy()
        for s in vertices:
            for t in vertices:
                if len(set([i,s,t])) == 3: # unique i s t
                    newdist[(s,t)] = min(dist[(s,t)], dist[(s,i)]+dist[(i,t)])
        dist = newdist
    return dist

if __name__ == '__main__':
    graph1 = {
        's': {'a': 5},
        'a': {'b': 3},
        'b': {'d': 4, 'c': -6},
        'c': {'a': 2, 'e': 5}
    }
    dist1 = floyd_warshall(graph1)
    print(dist1)

    # example from Algs4 Robert Sedgewick
    graph2 = {
        0: {1: 5.0,  4: 9.0,  7: 8.0},
        1: {2: 12.0, 3: 15.0, 7: 4.0},
        2: {3: 3.0,  6: 11.0},
        3: {6: 9.0},
        4: {5: 4.0,  6: 20.0, 7: 5.0},
        5: {2: 1.0,  6: 13.0},
        6: {}, 
        7: {2: 6.0,  5: 7.0},
    }
    dist2 = floyd_warshall(graph2)
    print(dist2)