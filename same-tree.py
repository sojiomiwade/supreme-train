# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
same => p and q are null => return true
        if one is null => return false
        if pval is not qval => return false
        now recurse: return same(pleft,qleft) and same(pright,qrit)
if they are both null, no recursive calls
       1      1
      /      / \
     2     2    3
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val==q.val and (
            self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

            # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
same => p and q are null => return true
        if one is null => return false
        if pval is not qval => return false
        now recurse: return same(pleft,qleft) and same(pright,qrit)
if they are both null, no recursive calls
       1      1
      /      / \
     2     2    3
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val==q.val and (
                self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        return p is q
            

            # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
check pval equals qval
stp,stq
                   1
                 /   \
                2     3 
                     / \
                    4   5

                   1
                 /   \
                2     3 
                     / \
                    4   5
1 2 3 4 5
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pst,qst=[p],[q]
        while pst and qst:
            p=pst.pop()
            q=qst.pop()
            if not p and not q:
                continue
            if p and q and p.val==q.val:
                pst.append(p.right)
                pst.append(p.left)
                qst.append(q.right)
                qst.append(q.left)
            else:
                return False
        return True