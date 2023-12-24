# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
9:38 - 10:01 = 23

'''
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def find_nodes(
            curr: Optional[TreeNode],
            curr_par: Optional[TreeNode],
            curr_depth: int,
            res: Tuple[TreeNode, TreeNode, int, int]
        ) -> None:
            if res[0] and res[1]:
                return
            if not curr:
                return
            if curr.val == x:
                res[0] = curr_par
                res[2] = curr_depth
            if curr.val == y:
                res[1] = curr_par
                res[3] = curr_depth
            find_nodes(curr.left, curr, curr_depth + 1, res)
            find_nodes(curr.right, curr, curr_depth + 1, res)
            return
                
        res = [None, None, 0, 0]
        find_nodes(root, None, 0, res)
        parx, pary, depthx, depthy = res
        return depthx == depthy and parx is not pary
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def iscousins(cur: Optional[TreeNode]):
            if cur:
                if cur.val==x:
                    return (0,INT_MAX)
                if cur.val==y:
                    return (INT_MAX,0)
                xleft,yleft=iscousins(cur.left)
                xright,yright=iscousins(cur.right)
                return (1+min(xleft,xright),1+min(yleft,yright))
            return INT_MAX

        INT_MAX=2**31-1
        return iscousins(root)
