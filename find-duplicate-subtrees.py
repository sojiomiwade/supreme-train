# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
md5 hash
      2
    3.   n
  3.  n
3.  n
3n3n3n2
'''
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def finddups(node):
            if not node:
                return '#'
            s=finddups(node.left)
            s+=finddups(node.right)
            s+=f'{node.val}|'
            lookup[s].append(node)
            return s

        ans,lookup=[],defaultdict(list)
        finddups(root)
        for nodes in lookup.values():
            if len(nodes)>1:
                ans.append(nodes[0])
        return ans
