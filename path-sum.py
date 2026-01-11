# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#       5  9
#     /    
#    4      
# q = [(5, 13)-pop- (4,13-5), (8, 13-5)]
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        q = deque([(root, targetSum)])
        while q:
            root, target = q.popleft()
            if not root.left and not root.right and root.val == target:
                return True
            if root.left:
                q.append((root.left, target - root.val))
            if root.right:
                q.append((root.right, target - root.val))
        return False

