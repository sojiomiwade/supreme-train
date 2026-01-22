# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# depth is min depth of (left, right), when both exist
# otherwise, it is max depth of left, right; because a zero depth is not a depth
# 1 -- 0  
#   2 -- 1 
#     3 -- 2
# lfs, the first one you find is the answer
# expect 3
# q [3]
# level 3
# r []
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        q = [root]
        while q:
            level += 1
            r = []
            for node in q:
                if not node.left and not node.right:
                    return level
                if node.left:
                    r.append(node.left)
                if node.right:
                    r.append(node.right)
            q = r
        return -1
