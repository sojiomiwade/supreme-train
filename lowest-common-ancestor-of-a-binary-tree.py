# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
given a binary tree, find LCA
flag up means i am p or q
if i have my flag up, then i could be the LCA(since q could be downstream of me), so return me
but as a root, if both guys have their hands up, then i am the LCA
even with duplicate nodes in tree, i still have one LCA

key thing is if left and right have the flag up, then i am the LCA
but if only one of them do (or me does), then that one has to be the LCA
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
                    5
                2/     \
               (2)       3
              /   \    
             1     (4)
             ans=2

        '''
        if not root:
            return None
        if root in (p,q):
            return root # cannot be "p or q", it has to be the specific anc
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right
