'''
        xA    <-- as parent, mark right as none; per xA, no parent action
      /   \
     B    xC  <-- as child, put my left and right into the forest list
    / \   / \
   D  xE  F  G


res = [F, G, B]
or better for each node, print the (val,left-val,right-val)
[(F,null,null) (G,null,null), (B,D,null)]
'''
from __future__ import annotations
from typing import List, Optional


class TreeNode:
    def __init__(self, val, 
            left: Optional[TreeNode]=None,
            right: Optional[TreeNode]=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def should_delete(node: Optional[TreeNode]) -> bool:
    return node is not None and node.val in ('C', 'A', 'E')

def _delete_nodes(root: Optional[TreeNode], 
        forest: List[TreeNode]) -> None:
    '''
        xA    <-- as parent, mark right as none; per xA, no parent action
      /   \
     B    xC  <-- as child, put my left and right into the forest list
    / \   / \
   D  xE  F  G

   B.right = null
   forest=[F,G,B]
    '''
    if root:
        _delete_nodes(root.left, forest)
        if should_delete(root.left):
            root.left = None

        _delete_nodes(root.right, forest)
        if should_delete(root.right):
            root.right = None

        if should_delete(root):
            if root.left:
                forest.append(root.left)
            if root.right:
                forest.append(root.right)
        

def delete_nodes(root: TreeNode) -> List[TreeNode]:
    forest = []
    _delete_nodes(root, forest)
    if not should_delete(root):
        forest.append(root)
    return forest

tb = TreeNode('B', TreeNode('D'), TreeNode('E'))
tc = TreeNode('C', TreeNode('F'), TreeNode('G'))
tree = TreeNode('A', tb, tc)
forest = delete_nodes(tree)
for node in forest:
    node_left_val = node.left.val if node.left else None
    node_right_val = node.right.val if node.right else None
    print(f'{(node.val, node_left_val, node_right_val)}')
#[(F,null,null) (G,null,null), (B,D,null)]
'''
        xA    <-- as parent, mark right as none; per xA, no parent action
      /   \
     B    xC  <-- as child, put my left and right into the forest list
    / \   / \
   D  xE  F  G
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
if my child is in del list, mark it as null
key approach, add me to the forest only after recursively considering
children

2.right=null
forest=[]

'''
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def delNodes(root):
            if root:
                delNodes(root.left)
                delNodes(root.right)
                if root.left and root.left.val in todel:
                    root.left=None
                if root.right and root.right.val in todel:
                    root.right=None
                if root.val in todel:
                    if root.left:
                        forest.append(root.left)
                    if root.right:
                        forest.append(root.right)
        forest=[]
        todel=set(to_delete)
        delNodes(root)
        if root and root.val not in todel:
            forest.append(root)
        return forest