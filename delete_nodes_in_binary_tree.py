'''
        xA
      /   \
     B    xC
   /   \  /  \
  D    E F    G

        B
      /   \
     D     E 
{F, G, B}
'''
from typing import Set


class TreeNode:
    def __init__(self) -> None:
        ...

def should_delete(n: TreeNode) -> bool:
    ...

def delete_nodes(root: TreeNode) -> Set[TreeNode]:
    ...


root = ...