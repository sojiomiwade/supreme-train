# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
exp forests=[a,f,g]
forests=[a,]
key here is: 
1. if a node is a root, and not to be deleted, it can
    be added to forest. 
2. if a node is to be deleted return None
               a
            /     \
           b      Xc
         /   \   /   \
        d    Xe f     g 
'''
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def delNodes(root, is_a_root):
            if not root:
                return None
            delete_me=root.val in todel
            root.left=delNodes(root.left,delete_me)
            root.right=delNodes(root.right,delete_me)
            if is_a_root and not delete_me:
                forest.append(root)
            return None if delete_me else root
        forest,todel=[],set(to_delete)
        delNodes(root,True)
        return forest