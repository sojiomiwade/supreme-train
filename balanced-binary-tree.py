# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# need depth of every subtree
# can actually use a bfs? no
# any node: 
#     if any subtree return vals are -1, return -1
#     return -1 the 2 subtrees have depths differing by more than 1
# complexity: n
#          1
#        2   3 
#     4

class Solution:
    def isbalanced(self, node) -> int:
        if not node:
            return 0
        lval = self.isbalanced(node.left)
        rval = self.isbalanced(node.right)
        if lval == -1 or rval == -1 or abs(lval-rval) > 1:
            return -1
        return 1 + max(lval, rval)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isbalanced(root) != -1