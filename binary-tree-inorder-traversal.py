# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
                 2
                / \
               3   4
              /   /
             5   6
53264

st=[]
(4)(6)
53264

1
  \
   2
  /
3
exp: 132
st : [n(2)3
root : 2
res : [132]
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[root]
        res=[]
        while st:
            root=st.pop()
            if type(root) is int:
                res.append(root)
            elif root:
                st.append(root.right)
                st.append(root.val)
                st.append(root.left)
        return res# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
           1
        /     \
       4       2
        \     /  \
         7   3    5

res : 471325
root: n
st  : 

while st has elements
    go along left slide until until next left is null
    root = pop from stack
    put root into result
    push root.right to stack if right isn't null

'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st,res=[],[]
        while st or root:
            while root:
                st.append(root)
                root=root.left
            root=st.pop()
            res.append(root.val)
            root=root.right
        return res