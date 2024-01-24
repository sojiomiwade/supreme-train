"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
def cg(node)
    if node
        clonenode=Node()
        for all children of node
            clonenode.neighbors.append(cg(child))

how to handle already created nodes?
everyone does their pointing
clookup={1:c1,2:c2}
c1 -- c2
|      |
        c3
'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clonegraph(node):
            if node in clookup:
                return clookup[node]
            cnode=Node(node.val)
            clookup[node]=cnode
            for nb in node.neighbors:
                cnb=clonegraph(nb)
                cnode.neighbors.append(cnb)
            return cnode
        clookup={}
        return clonegraph(node) if node else None