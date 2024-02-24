# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
  1
2   3
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root:
                traverse(root.left)
                traverse(root.right)
                res.append(root.val)
        res=[]
        traverse(root)
        return res