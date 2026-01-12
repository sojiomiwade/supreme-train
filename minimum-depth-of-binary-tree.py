# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# depth is min depth of (left, right), when both exist
# otherwise, it is max depth of left, right; because a zero depth is not a depth
# 1 
#   2
#     3
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        
