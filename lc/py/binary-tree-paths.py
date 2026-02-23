from typing import List, Optional
# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# when u get to the end put it in ans
# it: s -- keep appending/popping from s
# when hit leaf node add s to ans 

# base case: if none return 
# base case: leaf node: add urself, then add list to ans, then pop urself
# normal case: add urself, go

# ans []
# nodes [1 2 5]
# root 2
class Solution:
    def helper(self, nodes: List[int], root: Optional[TreeNode], ans: List[str]):
        if not root:
            return
        if not root.left and not root.right:
            nodes.append(root.val)
            ans.append("->".join(str(v) for v in nodes))
            nodes.pop()
            return
        nodes.append(root.val)
        self.helper(nodes, root.left, ans)
        self.helper(nodes, root.right, ans)
        nodes.pop()
        

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        nodes, ans = [], []
        self.helper(nodes, root, ans)
        return ans
