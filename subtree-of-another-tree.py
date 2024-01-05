# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
for all nodes in the root, see if similar_tree(node, subRoot)
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issimilar(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val==y.val and issimilar(x.left,y.left) and issimilar(x.right,y.right)

        def preorder(cur):
            if cur:
                ans=issimilar(cur, subRoot)
                ans=ans or preorder(cur.left)
                ans=ans or preorder(cur.right)
                return ans
            return False

        return preorder(root)