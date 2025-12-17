# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
can make a code of each root, with counter to count duplicates. 
at the end return all nodes with count value > 1
    2
  /   \
 4     3
2: 2 + hash(4) + hash(3)
if null, no hash. 
now pre vs in vs post
      1
    /   \ 
   0     0
0|1|0 vs 100
      0
     /
    1
   /
  0
0|1|0 vs 010
0|1|0|
0|1|0|31
3
count {02:}

            0
         /     \
        0       0
       /         \
      0           0
                   \
                    0
nodes 0||
'''
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def find_dups(root: Optional[TreeNode]) -> str:
            if not root:
                return 'X'
            code=f'{str(root.val)}|{find_dups(root.left)}|{find_dups(root.right)}|'
            nodes[code].append(root)
            return code

        nodes=defaultdict(list)
        find_dups(root)
        return [nodes_[0] for nodes_ in nodes.values() if len(nodes_)>1]