'''
          20
        /    \
       9     25
     /   \     
    5    12
        /  \
       11  14
       
approach: do a search for num, and set ans to the node in search if that node is 
smaller than num, but bigger than ans
if at the end of while, ans is not set, return -1
'''
class BST:
  def find_largest_smaller_key(self, num):
    ans=float('-inf')
    cur=self.root
    while cur:
      if cur.key<num:
        ans=max(ans,cur.key)
      if num>cur.key:
        cur=cur.right
      else:
        cur=cur.left
    if ans==float('-inf'):
      return -1
    return ans
