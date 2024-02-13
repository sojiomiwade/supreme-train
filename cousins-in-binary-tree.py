# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
can use BFS inserting (x,depth)
or just DFS, and when we find either recall the depth
'''
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xdep=ydep=None
        q=deque([(root,0,None)])
        while q:
            u,udep,upar=q.popleft()
            if u.val==x:
                xdep,xpar=udep,upar
            elif u.val==y:
                ydep,ypar=udep,upar
            q.extend([(v,udep+1,u) for v in (u.left,u.right) if v])
        assert None not in (xdep,ydep)
        return xdep==ydep and xpar is not ypar