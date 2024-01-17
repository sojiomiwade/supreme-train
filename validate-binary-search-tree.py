# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
first: do an inorder, and validate. time, space = n, n
better: as we inorder can we just check the cur element against the last?
perhaps pass the last to inorder. can return false immediately when last>=cur.
otherwise keep going
            1
          /
        1
        lis=[-inf,]
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(node):
            if not node:
                return True
            ans=isvalid(node.left)
            if lis[-1]>=node.val:
                return False
            lis.append(node.val)
            ans=ans and isvalid(node.right)
            return ans

        lis=[float('-inf')]
        return isvalid(root)