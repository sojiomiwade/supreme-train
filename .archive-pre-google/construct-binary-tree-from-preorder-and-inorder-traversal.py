# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#preorder holds the roots
'''
               3
            /     \
           9      20
                 /  \
               15    7 

buildtree(lo, rootloc-1) 
passing the tree bounds makes us know when to stop 
    building down the left and move to right
3 9 4
inorder  [9 3 4]
preorder [3 9 4 ]
inol {90 31 42}
               3
            /     \
pre [9 4]
bt (0 2)
            3
            / \
         (00) (11)

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildtree(lo, hi):
            if lo>hi:
                return None
            root=TreeNode(pre.popleft())
            irloc=inol[root.val]
            root.left=buildtree(lo,irloc-1)
            root.right=buildtree(irloc+1,hi)
            return root
        inol={inoval:idx for idx,inoval in enumerate(inorder)}
        pre=collections.deque(preorder)
        root=buildtree(0,len(inol)-1)
        assert not pre
        return root
    