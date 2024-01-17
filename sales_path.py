'''
need to consider every path and return the mincost path
time,space=O(V+E),O(V+E) via DFS for example
if we find better replace the current
cost[i] = mycost+mincost of my children
if root:
  update mincost
'''
def get_cheapest_cost(rootNode):
  minchildcost=float('inf') if rootNode.children else 0
  for chnode in rootNode.children:
    minchildcost=min(minchildcost,get_cheapest_cost(chnode))
  return rootNode.cost+minchildcost
  
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

n51,n31,n61=Node(5),Node(3),Node(6)
n42,n22,n02,n12,n52=Node(4),Node(2),Node(10),Node(1),Node(5)
n51.children=[n42]
n31.children=[n22,n02]
n61.children=[n12,n52]
children=[n51,n31,n61]
root=Node(0)
root.children=children

print(get_cheapest_cost(root)) #3