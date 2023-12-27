# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
                1 [0,null]
             /     \
            2       3           (,)
             \     /
              4   5
same depth => true, but if same parent => false
res=(xpar,ypar,xdep,ydep)
'''
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def isCousins(cur,dep,par):
            nonlocal xpar,ypar,xdep,ydep
            if (xpar and ypar) or not cur:
                return
            if cur.val==x:
                xpar,xdep=par,dep #2,2
            elif cur.val==y:
                ypar,ydep=par,dep
            isCousins(cur.left,dep+1,cur)
            isCousins(cur.right,dep+1,cur)

        xpar,ypar,xdep,ydep=None,None,-1,-1
        isCousins(root,0,None)
        return xpar is not ypar and xdep==ydep