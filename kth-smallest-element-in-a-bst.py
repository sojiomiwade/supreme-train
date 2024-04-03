# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
use a count that passed around
if u get a value back, that's the ans

count,node (1 3)
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def ksmallest(count: int, node: Optional[TreeNode]):
            if not node:
                return count
            count=ksmallest(count,node.left)
            if count<=0:
                return count
            if count==k:
                return -node.val
            return ksmallest(1+count,node.right)
        return -ksmallest(1,root)