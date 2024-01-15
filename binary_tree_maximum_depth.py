# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
          1
        /   \
             2
dep : 1
q : [2]
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([(1,root)])
        while q:
            dep,x=q.popleft()
            if x.left:
                q.append((1+dep,x.left))
            if x.right:
                q.append((1+dep,x.right))
        return dep
        # if not root:
        #     return 0
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))