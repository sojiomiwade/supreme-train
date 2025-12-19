'''
can bottom up this
a node's mincost is the minchild cost, and do this recursively
'''
def get_cheapest_cost(rootNode):
  def gcc(root):
    if not root:
      return 0
    mincost=MAXCOST
    for child in root.children:
      mincost=min(gcc(child),mincost)
    return root.cost+(0 if mincost==MAXCOST else mincost)
  MAXCOST=1+100000
  return gcc(rootNode)
########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################


# A node 
class Node:
  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
 
root=Node(0)
five=Node(5)
three=Node(3)
two=Node(2)
two.children=[Node(2)]
three.children=[two,Node(10)]
six=Node(6)
root.children=[five,three,six]

print(get_cheapest_cost(root)) # 3