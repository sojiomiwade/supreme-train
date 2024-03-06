# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
determine if val is going left or right.
if going left
    if left
        set cur to left
    else 
        cur.left is a new node with value equal val
        break
else (oing right)
fishes

cur 7
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur=root
        while True:
            if val<cur.val:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=TreeNode(val)
                    break
            else:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=TreeNode(val)
                    break
        return root