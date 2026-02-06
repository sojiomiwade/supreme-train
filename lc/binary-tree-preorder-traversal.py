# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
#                1
#             /     \
#            2       3
#          /   \      \
#         4     5      6
# stack for what to process "next"
# set root to the left on each iteration, and then put the right on stack
# if no root to process, then pop stack into root for processing
# ans [1 2 4 5 3 6]
# r 
# st [6]

# ans [1 2 3]
# r x
# s []
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # s = []
        # while root or s:
        #     if not root:
        #         root = s.pop()
        #     else:
        #         ans.append(root.val)
        #         s.append(root.right)                
        #         root = root.left
        # return ans

        def preo(root: Optional[TreeNode]) -> None:
            if not root:
                return
            ans.append(root.val)
            preo(root.left)
            preo(root.right)

        ans = []
        preo(root)
        return ans      