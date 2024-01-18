# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
for each node in root with value equal to subRoot.val (via DFS), do a DFS to see if similar, and break early
instead of DFS could use BFS for both
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issubtree(node,subnode):
            if not node and not subnode:
                return True
            if not node or not subnode: 
                return False
            assert node and subnode
            ans=node.val==subnode.val
            ans=ans and issubtree(node.left,subnode.left)
            ans=ans and issubtree(node.right,subnode.right)
            return ans

        def issubtree_filter(node):
            if not node:
                return False
            if issubtree(node,subRoot):
                return True
            return issubtree_filter(node.left) or issubtree_filter(node.right)

        return issubtree_filter(root)