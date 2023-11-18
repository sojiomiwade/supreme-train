"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

1 - 2
|   |  
3 - 4

1 - 2
|   |
3 - 4

can use DFS. 
clone the curr node. then
seems the parent is going to be passed so that 

2--4

1--3
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def _clonegraph(u,uc):
            for v in u.neighbors:
                if v not in clookup:
                    clookup[v]=Node(v.val)
                vc=clookup[v]
                uc.neighbors.append(vc)
                if v not in vis:
                    vis.add(v)
                    _clonegraph(v,vc)

        if not node:
            return None
        vis={node}
        nc=Node(node.val)
        clookup={node:nc}
        for nb in node.neighbors:
            if nb not in clookup:
                clookup[nb]=Node(nb.val)
            nbc=clookup[nb]
            nc.neighbors.append(nbc)
            if nb not in vis:
                vis.add(nb)
                _clonegraph(nb,nbc)

        return nc"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

1 - 2
|   |  
3 - 4

1 - 2
|   |
3 - 4

can use DFS. 
clone the curr node. then
seems the parent is going to be passed so that 

2--4


1---2
|   |
4---3
clookup={1:1c,2:2c,}
1<--2
^   ^
    v 
4<->3
cg(2,2c)

"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def _clonegraph(u,uc):
            for v in u.neighbors:
                if v not in clookup:
                    clookup[v]=Node(v.val)
                    _clonegraph(v,clookup[v])
                uc.neighbors.append(clookup[v])

        if not node:
            return None
        nc=Node(node.val)
        clookup={node:nc}
        for nb in node.neighbors:
            if nb not in clookup:
                clookup[nb]=Node(nb.val)
                _clonegraph(nb,clookup[nb])
            nc.neighbors.append(clookup[nb])
        return nc