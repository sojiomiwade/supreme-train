# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
               3
            /     \ 
           9       20
                  /   \
                 15    7
h(9) 1

       1
     /   \
    4     2
   /       \
  5         3


'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if abs(depth(node.left)-depth(node.right))<=1:
                return 1+max(depth(node.left),depth(node.right))
            return float('inf')
        if not root:
            return True
        return abs(depth(root.left)-depth(root.right))<=1