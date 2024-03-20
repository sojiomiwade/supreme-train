# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
inorder [9352], postorder [9253]
expected
           3
        /     \
       9       5
                \
                 2
postorder [92]
lloc {90 31 52 23}
lo,hi 03 --> 00 --> 01 --> 0
root,rootloc 31 --> 52 --> 23
           3
        /     \ 
               5
                \
                 2
        
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildtree(lo: int, hi: int) -> Optional[TreeNode]:
            if lo>hi:
                return None
            root=TreeNode(postorder.pop())
            rootloc=lloc[root.val]
            root.right=buildtree(rootloc+1,hi)
            root.left=buildtree(lo,rootloc-1)
            return root

        lloc={x:idx for idx,x in enumerate(inorder)}
        return buildtree(0,len(postorder)-1)