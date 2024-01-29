  def find_in_order_successor(self, inputNode):
    '''
    takes node, returns node
    9 : 11 --> go to the right, then go as left as possible
    12: 14
    
    5 : 9 --> if no right, find first parent bigger than you
    11 : 12
    14: 20
    25: null
    '''
    assert inputNode
    if inputNode.right:
      cur=inputNode.right
      while cur:
        ans=cur
        cur=cur.left
      return ans
    cur=inputNode.parent
    while cur:
      if cur.key>inputNode.key:
        return cur
      cur=cur.parent
    return None      
