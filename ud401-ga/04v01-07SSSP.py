"""
SSSP = single source shortest path

Dijkstra's alg, similar to BFS, explore graph in layered approach 

BFS/DFS takes O(V+E) time

Dijkstra's alg need to use minheap, O((V+E)log(V))

Dijkstra's alg doesn't work for negative weight edges

walk = repeat vertices, path=no repeat vertices

DP single source shortest path

shortest path p from s to z

for 0 ≤ i ≤ n-1 and z in V:
    D(i,z) = length of shortest path from s to z using ≤ i edges

base case: D(0,s) = 0 and for z≠s, D(0,z) = ∞

for i ≥ 1: compute path s->z using i edges

s -----> y -----> z
D(i-1,y)   w(y,z)

D(i,z) = min{ D(i-1,y)+w(y,z) }

to meet the definition of D (path ≤i edges, not =i edges), change recurrence to

D(i,z) = min{ D(i-1,y)+w(y,z), D(i-1,z)}

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

def bellman_ford0(graph, s):
    vertices = extract_vertices(graph)
    reverse_graph = extract_reverse_graph(graph, vertices)
    n = sum(len(dest) for dest in graph.values())
    dist = {v:inf for v in vertices}
    dist[s] = 0
    for i in range(n-1):
        newdist = {}
        for z in vertices:
            newdist[z] = dist[z]
            for y in reverse_graph[z]:
                newdist[z] = min(newdist[z], dist[y] + graph[y][z])
        dist = newdist
    return dist

# if nth iter of dist != (n-1)th iter of dist
# then has negative cycle
def bellman_ford1(graph, s):
    vertices = extract_vertices(graph)
    reverse_graph = extract_reverse_graph(graph, vertices)
    n = sum(len(dest) for dest in graph.values())
    dist = {v:inf for v in vertices}
    olddist, newdist = None, None
    dist[s] = 0
    for i in range(n):
        newdist = {}
        for z in vertices:
            newdist[z] = dist[z]
            for y in reverse_graph[z]:
                newdist[z] = min(newdist[z], dist[y] + graph[y][z])
        olddist, dist = dist, newdist
    if olddist != dist:
        print('has negative cycle')
    return olddist

if __name__ == '__main__':
    graph1 = {
        's': {'a': 5},
        'a': {'b': 3},
        'b': {'d': 4, 'c': -6},
        'c': {'a': 2, 'e': 5}
    }
    dist1 = bellman_ford1(graph1, 's')
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
    dist2 = bellman_ford1(graph2, 0)
    print(dist2)







