# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
root 3
res [[3] [15 7]]
level [9 20]
q  | 15 7
node 20
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root: return []
        # q=deque([root])
        # res=[]
        # while q:
        #     level=[]
        #     for _ in range(len(q)):
        #         node=q.popleft()
        #         level.append(node.val)
        #         q.extend([child for child in (node.left,node.right) if child])
        #     res.append(level)
        # return res


