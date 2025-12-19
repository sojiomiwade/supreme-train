# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# return 
# root if any of the twoo hold
#     - root is p or q 
#     - lcaleft and lcaright both have it
# lcaleft or lcaright
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root in (p,q):
            return root
        lcaleft=self.lowestCommonAncestor(root.left,p,q)
        lcaright=self.lowestCommonAncestor(root.right,p,q)
        if lcaleft and lcaright:
            return root
        return lcaleft or lcaright