# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
when you get to a leaf, check if we have it
set up a tree dfs first
            1
           /
          2

            5
          /
         4
        /
      11
        \
         2
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def search(node: TreeNode, cur: int):
            if not node.left and not node.right:
                return cur+node.val==targetSum
            left=node.left and search(node.left,cur+node.val) 
            right=node.right and search(node.right,cur+node.val)
            return left or right
        if root:
            return search(root,0)    
        return False