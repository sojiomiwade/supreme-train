# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# (5, 22)
# 22 - 5 

#     5
#   /   \  
#  4     8
# at 4: 12 - 5 == 7
# at 4: 
# haspathsum(5, 12)
#     if 5 is nil: return false
#     if leaf, check 12 == 5, and return true / false
#     otherwise: 
#     return haspathsum(5.left, 12 - 5) or haspathsum(5.right, 12 - 5)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    