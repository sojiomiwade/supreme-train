# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
new buf for each level, use queue to track each level
level : [15 7]
cur: 20
buf : []
res : [[3],[9 20]]
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level,res=deque([root]),[]
        while level:
            buf=[]
            for i in range(len(level)):
                cur=level.popleft()
                buf.append(cur.val)
                if cur.left:
                    level.append(cur.left)
                if cur.right:
                    level.append(cur.right)
            res.append(buf[:])
        return res