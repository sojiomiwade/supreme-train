# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
  1
2   3
 5 
ans 1 3
depths 0 1
root,depth 3 1
runtime: O(n)
space: O(h) <-- depths
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def visit(root, depth):
            if root:
                if depth not in depths:
                    ans.append(root.val)
                    depths.add(depth)
                visit(root.right,depth+1)
                visit(root.left,depth+1)
        ans=[]
        depths=set()
        visit(root,0)
        return ans
