# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
first: recursive: append  left, then root.val, then right
    time,space: O(n),O(h+n)=O(n) since n>=h
second: iterative:
           1
        /     \
       2       3
      / \     / \
     .   4   5   .
              \
               6 
    ans=[2,4,1,5,6,3]
    st=[3 6] 
    root=
    next=(6)
    ans=[2 4 1 5 6]

    st=[]
    while st or root
        if root
            st.append(root)
            root=root.left
        else:
            next=st.pop()
            ans.append(next.val)
            root=next.right
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st,ans=[],[]
        while st or root:
            if root:
                st.append(root)
                root=root.left
            else:
                next=st.pop()
                ans.append(next.val)
                root=next.right
        return ans

        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         ans.append(root.val)
        #         inorder(root.right)

        # ans=[]
        # inorder(root)    
        # return ans