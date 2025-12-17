# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
              2 -- -1 0
            /   \
           -1   null
           res : 2

'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def mps(root):
            nonlocal res
            if not root:
                return 0
            mpsleft,mpsright=mps(root.left),mps(root.right)
            res=max(res,root.val+max(0,mpsleft,mpsright,mpsleft+mpsright))            
            return root.val+max(0,mpsleft,mpsright)
        
        res=float('-inf')
        mps(root)
        return res