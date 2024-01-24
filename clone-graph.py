"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

like in DFS, still need a lookup
only nodes that aren't in lookup go in queue
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clookup={node:Node(node.val)}
        q=deque([node])
        while q:
            x=q.popleft()
            cx=clookup[x]
            for nb in x.neighbors:
                if nb not in clookup:
                    q.append(nb)
                    clookup[nb]=Node(nb.val)
                cx.neighbors.append(clookup[nb])
        return clookup[node]