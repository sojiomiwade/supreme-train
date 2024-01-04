# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
0 : 3
1 : 9,
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def level_order(root,rootlevel):
            if root:
                level[rootlevel].append(root.val)
                level_order(root.left,rootlevel+1)
                level_order(root.right,rootlevel+1)

        level=defaultdict(list)
        level_order(root,0)
        return level.values()