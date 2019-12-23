"""
DFS, BFS
Dijkstra for single source shortest path
SCC on Digraph
Application: 2-SAT
MST
PageRank (Markov Chains)

Connected components in undirected graph G
    Run DFS and keep track of component#

"""
from collections import defaultdict

def edges_to_adjlist(edges):
    adjlist = defaultdict(list)
    for s,t in edges:
        adjlist[s].append(t)
        adjlist[t].append(s)
    return adjlist

def classic_dfs(graph):
    visited = set()
    start = list(graph.keys())[0]
    def dfs(graph, v):
        if v not in visited:
            visited.add(v)
            for t in graph[v]:
                dfs(graph, t)
    dfs(graph, start)
    return visited

def cc_dfs0(graph):
    # input: G = (V, E) in adj list representation
    # output: vertices labelled by connected components
    cc = 0
    ccnum = {}
    visited = set()
    def explore(z): # should be named dfs
        ccnum[z] = cc
        visited.add(z)
        for t in graph[z]:
            if t not in visited:
                explore(t) 
    for v in graph:
        if v not in visited:
            cc += 1
            explore(v)
    return ccnum

def cc_dfs1(graph): # base on classic_dfs
    cc = 0
    ccnum = {}
    visited = set()
    def dfs(v):
        if v not in visited:
            ccnum[v] = cc
            visited.add(v)
            for t in graph[v]:
                dfs(t)
    for v in graph:
        if v not in visited:
            cc += 1
            dfs(v)
    return ccnum

def cc_dfs2(graph): # save path, backtrack
    cc = 0
    ccnum = {}
    visited = set()
    track = {}
    def explore(z): # should be named dfs
        ccnum[z] = cc
        visited.add(z)
        for t in graph[z]:
            if t not in visited:
                track[t] = z
                explore(t) 
    for v in graph:
        if v not in visited:
            cc += 1
            explore(v)
    return ccnum, track

def cc_dfs3(graph):
    # prepare for digraph
    # preorder and postorder
    clock = 1
    pre, post = {}, {}
    visited = set()
    track = {}
    def explore(z): # should be named dfs
        nonlocal clock
        pre[z] = clock
        clock += 1
        visited.add(z)
        for t in graph[z]:
            if t not in visited:
                track[t] = z
                explore(t)
        post[z] = clock
        clock += 1
    for v in graph:
        if v not in visited:
            explore(v)
    return pre, post

def test0():
    edges = [(1,2), (2,3), (1,4), (3,4), (5,6)]
    adjlist = edges_to_adjlist(edges)
    print(adjlist)
    print(classic_dfs(adjlist))
    print(cc_dfs0(adjlist))
    print(cc_dfs1(adjlist))
    print(cc_dfs2(adjlist))
    print(cc_dfs3(adjlist))

if __name__ == '__main__':
    test0()


