'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

first approach: tree has V-1 edges, so we can just return true if E=V-1 and false otherwise. this assumes no self edges in list. but even then, we can filter those out
second approach: count number of connected components. true only if count is 1, and all nodes are in that components. no this won't suffice. you have to look at E count or in addition ensure no node in a visit call encounters a visited node that isn't its parent

'''

from typing import List, Optional, Set


def istree(nbs: List[List[int]]) -> bool:
    def hasscycle(v: int,parent:Optional[int]) -> bool:
        if visited[v]:
            return False
        visited[v]=True
        cycle=False
        for w in nbs[v]:
            if visited[w] and parent is not None and w!=parent:
                return True
            cycle=cycle or hasscycle(w,v)
        return cycle

    n=len(nbs)
    compcount=0
    visited=[False for _ in range(n)]
    cycle=hasscycle(0,None)
    return all(visited) and not cycle

def get_graph(n: int, edges: List[List[int]]) -> List[List[int]]:
    nbs=[[] for _ in range(n)]
    for v,w in edges:
        nbs[v].append(w)
        nbs[w].append(v)
    print(nbs)
    return nbs

def graph_valid_tree(n: int, edges: List[List[int]]) -> bool:
    nbs=get_graph(n,edges)
    return (istree(nbs))

n,edges = 5,[[0,1], [1,2], [2,3], [1,3], [1,4]]
print(graph_valid_tree(n,edges)) # false
n,edges = 5,[[0,1], [0,2], [0,3], [1,4]]
print(graph_valid_tree(n,edges)) # true
