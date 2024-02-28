'''
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

    1 v 
  /   \
v 2----3
      \
       4 nv

so if 3 sees someone that is visited other than its parent
then return false. otherwise, return true
'''

from typing import DefaultDict, List
from collections import defaultdict


def graph_valid_tree(edges: List[List[int]], n: int) -> bool:
    def buildgraph() -> DefaultDict[int,List]:
        nbs=defaultdict(list)
        for u,v in edges:
            nbs[u].append(v)
            nbs[v].append(u)
        return nbs

    '''
          1 
        /   \
       2-----3
              \
               4 
    node parent 32 21
    visited = {1 2 3}
    '''
    def validate(node: int, parent: int) -> bool:
        visited.add(node)
        for nb in nbs[node]:
            if nb in visited and nb != parent:
                return False
            if nb not in visited and not validate(nb, node):
                return False
        return True
        
    nbs=buildgraph()
    visited=set()
    return validate(0, None)
