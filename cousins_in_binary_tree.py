# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
            1
        2       3
      4        5

'''
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def iscousins(cur: Optional[TreeNode]):
            if cur:
                if cur.val==x:
                    return 0,INT_MAX
                if cur.val==y:
                    return INT_MAX,0
                if cur.left and cur.right and set([x,y])==set([cur.left.val,cur.right.val]):
                    return INT_MAX,INT_MAX
                xleft,yleft=iscousins(cur.left)
                xright,yright=iscousins(cur.right)
                return 1+min(xleft,xright),1+min(yleft,yright)
            return INT_MAX, INT_MAX

        INT_MAX=2**31-1
        xdep,ydep=iscousins(root)
        return xdep<INT_MAX and ydep<INT_MAX and xdep==ydep
