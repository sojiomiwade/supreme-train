"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
a - b   a <- b
|   |   ^    ^
d - e   d  > e   
clone {aa bb}
b on looping through cloned neighbors: b.append(clone[a])
b on looping through not cloned nbs: call clone to get the node, 
    then append
'''
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def cloneGraph(node):
            cnode=Node(node.val)
            clone[node]=cnode
            for nb in node.neighbors:
                if nb in clone:
                    cnode.neighbors.append(clone[nb])
                else:
                    cnb=cloneGraph(nb)
                    cnode.neighbors.append(clone[nb])
            return cnode

        if not node:
            return None
        clone={}
        return cloneGraph(node)