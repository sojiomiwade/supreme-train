# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
pi(x)!=pi(y) and depth(x)==depth(y)
just go find those four values. 
then in main function return the condition above
'''
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def preorder(node: Optional[TreeNode], depth: int, pi: int) -> None:
            nonlocal xpi,ypi,xdepth,ydepth
            if node:
                if node.val==x:
                    xdepth=depth
                    xpi=pi
                elif node.val==y:
                    ydepth=depth
                    ypi=pi
                preorder(node.left,1+depth,node.val)
                preorder(node.right,1+depth,node.val)
        xpi=ypi=xdepth=ydepth=None
        preorder(root,0,0)
        return xpi!=ypi and xdepth==ydepth