# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
               1
            /     \ 
           2       3
1(2)(3)

               1
            /     \ 
           2       3
1()(3)

               1
            /     \ 
           2       
1(2)


example 1: 1(2(4))(3)
example 2: 1(2()(4))(3)
'''
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        ans=str(root.val)
        if not root.left and not root.right:
            return ans
        ans+=f'({self.tree2str(root.left)})'
        if root.right:
            ans+=f'({self.tree2str(root.right)})'
        return ans