# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
parentheses not omitted only when tree has a right
root will always omit par on null children, except
    when that child is left and there is right
'''
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def tree2str(root, ans):
            if root:
                ans.append(str(root.val))
                
                if root.left or root.right:
                    ans.append('(')
                    tree2str(root.left,ans)
                    ans.append(')')

                if root.right:
                    ans.append('(')
                    tree2str(root.right,ans)
                    ans.append(')')

            return ans
        return ''.join(tree2str(root,[]))