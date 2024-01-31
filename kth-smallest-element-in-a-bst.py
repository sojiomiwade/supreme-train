# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
st -- do we have something to go back to
root -- i hit a null (doesn't mean we are done)
so loop on: 
- if htere's root, put it in stack and search further down the left
- otherwise, pop the stack, process the element, and set root to right
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
                    3
                 /     \ 
                1       4
                 \
                  2
          count=1
          root=3
        '''
        st=[];count=1
        while root or st:
            if root:
                st.append(root)
                root=root.left
            else:
                node=st.pop()
                if count==k:
                    return node.val
                count+=1
                root=node.right
        assert 0, f'{k} too big'
        # def inorder(root):
        #     nonlocal count
        #     if not root:
        #         return None
        #     ans=inorder(root.left)
        #     if ans:
        #         return ans
        #     count+=1
        #     if count==k:
        #         return root
        #     return inorder(root.right)
            
        # count=0
        # return inorder(root).val