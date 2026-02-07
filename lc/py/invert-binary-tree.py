# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# # dfs really easy
# # bfs just invert every node children
#             1
#           /
#          2
#         /
#        3
# a = [3]
# v = 3
#                 1
#                  \
#                   2
#                     \
#                      3
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = []
        if root:
            a.append(root)
        while a:
            v = a.pop()
            v.left, v.right = v.right, v.left
            if v.left:
                a.append(v.left)
            if v.right:
                a.append(v.right)
        return root