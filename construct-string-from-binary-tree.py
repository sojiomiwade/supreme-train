# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1(2()(4))(3)
[1,(2()(4))()]
idea: if there is nothing in right, omit the parentheses. otherwise dont
'''
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def tree2str(root):
            if root:
                res.append(str(root.val))
                if root.left or root.right:
                    res.append('(')
                    tree2str(root.left)
                    res.append(')')
                    if root.right:
                        res.append('(')
                        tree2str(root.right)
                        res.append(')')
        res=[]
        tree2str(root)
        return ''.join(res)