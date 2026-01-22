# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# stack? 
#                1
#              /   \
#             2     3
#            /     /
#           4    5
# if 
# if root is defined, push root onto stack, and set root to root.left
# else if stack is defined, pop-and-process, then set root to root.right if root.right is defined
# else break out, and return ans!!!
# 1
#  \ 
#   2
#  /
# 3
# st = []
# ans = [1 3 2]
# r = x
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, st = [], []
        while root or st:
            if root:
                st.append(root)
                root = root.left
            else:
                root = st.pop()
                ans.append(root.val)
                root = root.right
        return ans
        # def ino(node: Optional[TreeNode]) -> None:
        #     if node:
        #         ino(node.left)
        #         ans.append(node.val)
        #         ino(node.right)
        # ans = []
        # ino(root)
        # return ans

