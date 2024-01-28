# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
if roots have same value, and likewise for p.left q.left, and likewise for p.riht q.right. then they're the same
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        assert p and q
        issame = p.val == q.val
        issame = issame and self.isSameTree(p.left,q.left)
        issame = issame and self.isSameTree(p.right,q.right)
        return issame