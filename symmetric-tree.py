# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# call(r.l, r.r): (only if root is not nil)
#   func(l, r)
#     if both nil return true
#     if one is nil return false
#     if l.val != r.val return false
#     return both of: 
#         call(l.l, r.r) 
#         call(l.r, r.l) 
#      1
#    2   2
class Solution:
    def sym(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.sym(left.left, right.right) and self.sym(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root.left, root.right)
        