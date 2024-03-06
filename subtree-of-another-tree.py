'''
               3
            /     \
           4       5
         /   \
        1     2


3      4

time O(nm)
space O(h1*h2)
traverse first tree and inside that one traverse the second
'''
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            return root.val==subroot.val and issame(root.left,subroot.left) and issame(root.right,subroot.right)
        
        def trav(root):
            return (issame(root,subRoot) or 
                (root and (trav(root.left) or trav(root.right))))

        return trav(root)