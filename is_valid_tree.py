'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

0 -- 1 -- 2 -- 3
     \________/
     \___________ 4
time: 8:16 -- 
is there a cycle in the graph? 
for each node: 
    DFS such that if you ever about to color a colored node, return F
'''

from collections import defaultdict


def is_valid_tree(n, edges):
    def dfs_cycle(node) -> bool:
        visit.add(node)
        for nb in nbs[node]:
            if nb in visit:
                 if parent[node] != nb:
                    return True
            else:
                parent[nb] = node
                print('dfs cycle', node, nb)
                if dfs_cycle(nb):
                    return True
        return False

    nbs = defaultdict(set)
    for (u,v) in edges:
        nbs[u].add(v)
        nbs[v].add(u)
    visit = set()
    parent = {}
    is_cycle = dfs_cycle(edges[0][0])
    print('is cycle', is_cycle)
    print('visit', visit)
    print('nbs', nbs)
    if is_cycle or len(visit) != n:
        return False
    return True

n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
print(is_valid_tree(n, edges)) # false, cycle

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(is_valid_tree(n, edges)) # true

n = 3
edges = [[0,1],[2,3]]
print(is_valid_tree(n, edges)) # false, disconnected

