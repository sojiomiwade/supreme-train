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
