# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
            3
         /     \ 
        1       4
         \
          2
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            nonlocal count
            if not root:
                return None
            ans=inorder(root.left)
            if ans:
                return ans
            count+=1
            if count==k:
                return root
            return inorder(root.right)
            
        count=0
        return inorder(root).val