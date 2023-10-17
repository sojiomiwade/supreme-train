from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int,
        left: Optional[Node]=None,
        right: Optional[Node]=None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

def inorder(node: Optional[Node], res: List[int]) -> None:
    if node:
        inorder(node.left, res)
        res += [node.val]
        inorder(node.right, res)

def preorder(node: Optional[Node], res: List[int]) -> None:
    if node:
        res += [node.val]
        preorder(node.left, res)
        preorder(node.right, res)

def postorder(node: Optional[Node], res: List[int]) -> None:
    if node:
        postorder(node.left, res)
        postorder(node.right, res)
        res += [node.val]
'''
             5
           /   \
          3     7
           \   /
            4 6
'''
left = Node(3, None, Node(4))
right = Node(7, Node(6), None)
root = Node(5, left, right)
ordered = []
preorder(root, ordered)
print(ordered)
ordered = []
postorder((root), ordered)
print(ordered)
ordered = []
inorder(root, ordered)
assert  ordered == sorted(ordered)
