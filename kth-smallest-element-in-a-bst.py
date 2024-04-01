# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
5
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthsmallest(root, idx) -> Tuple[bool, int]:
            if not root:
                return (False,idx)
            found,idx=kthsmallest(root.left,idx)
            if found:
                return (True, idx)
            if idx==k:
                return (True,root.val)
            return kthsmallest(root.right,idx+1)
        return kthsmallest(root,1)[1]