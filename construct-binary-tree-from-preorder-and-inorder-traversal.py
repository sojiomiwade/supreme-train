# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
pre : 3   9   20   15   7
ino : 9   3   15   20   7
take from pre and make a root
call buildtree on array to left in ino, and array to right of ino
               3
            /     \
           9        [15 20 7] pre -> 20 -> (20) 
                   /   \
                  [15] [7]

preidx=0
there's a ilo and ihi (for in order range)

test
should have
            3
          /   \
         9     1
iil={9:0,3:1,1:2}
pre 3 9 1
ino 9 3 1
preidx=2
lo,mi,hi=0 0 2
            3
          /   \
         9
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildtree(lo: int, hi: int) -> Optional[TreeNode]:
            nonlocal preidx
            if lo>hi:
                return None
            root=TreeNode(preorder[preidx])
            preidx+=1
            mi=iilookup[root.val]
            root.left=buildtree(lo,mi-1)
            root.right=buildtree(mi+1,hi)
            return root

        preidx=0
        iilookup={x:i for i,x in enumerate(inorder)}
        lo,hi=0,len(inorder)-1
        return buildtree(lo,hi)