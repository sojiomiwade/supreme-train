# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
best perhaps seen as postorder (children first then me)
if children are processed, ok, so now i can set them to null
parent sets children to null, as needed, 
children can add themselves to forest
1-2-3-4
'''
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def delNodes(root,forest):
            if root:
                delNodes(root.left,forest)
                delNodes(root.right,forest)

                if root.val in to_delete_set:
                    if root.left and root.left.val not in to_delete:
                        forest.append(root.left)
                    if root.right and root.right.val not in to_delete:
                        forest.append(root.right)

                if root.left and root.left.val in to_delete:
                    root.left=None
                if root.right and root.right.val in to_delete:
                    root.right=None
            return forest
        to_delete_set=set(to_delete)
        forest=[]
        if root and root.val not in to_delete_set:
            forest.append(root)
        return delNodes(root,forest) 