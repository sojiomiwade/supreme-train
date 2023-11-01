# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        when you get to leaf, update max, so pass max
        also, back track for various branches
        can avoid stack and use BFS
                 1
                /\
               2  3
              /\  /\
             4  ..  5
        '''
        if not root:
            return 0
        q = deque([root])
        maxdepth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxdepth += 1
        return maxdepth
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))