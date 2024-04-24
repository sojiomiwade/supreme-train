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
         \
          2
           \
            3
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if abs(height(node.left)-height(node.right))<=1:
                return 1+max(height(node.left),height(node.right))
            return float('inf')
        if not root:
            return True
        return abs(height(root.left)-height(root.right))<=1