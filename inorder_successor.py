#time: 12:56 -- 1:22 = 26 mins
# 1:09 = 13 to get it all squar (algorithm)
#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################

# A node
'''
always! go to the right node, and go left all the way
updating ans, where ans starts at the right node

go to the right node, and go left all the way left. ans is last node on this path
if no right node, ans is first ancestor such that anc > v. 
if no such exists return null

which wins parent or. right??


for any node v, if v.parent > v (v == v.parent.left)
then v.parent > v.right

'''
class Node:

  # Constructor to create a new node
  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
    self.root = None 

  def find_in_order_successor(self, inputNode):
    pass # your code goes here

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid 
  # using reference parameters)
  def insert(self, key):
    
    # 1) If tree is empty, create the root
    if (self.root is None):
      self.root = Node(key)
      return
        
    # 2) Otherwise, create a node with the key
    #    and traverse down the tree to find where to
    #    to insert the new node
    currentNode = self.root
    newNode = Node(key)
    while(currentNode is not None):
      
      if(key < currentNode.key):
        if(currentNode.left is None):
          currentNode.left = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.left;
      else:
        if(currentNode.right is None):
          currentNode.right = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.right;

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
  def getNodeByKey(self, key):
    
    currentNode = self.root
    while(currentNode is not None):
      if(key == currentNode.key):
        return currentNode
        
      if(key < currentNode.key):
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
        
    return None
  
  '''
  go to the right node, and go left all the way left. ans is last node on this path
  if no right node, ans is first ancestor such that anc > v. 
  if no such exists return null
  '''
  def find_in_order_successor(self, node):
    res = node.right
    if res:
      while res.left:
        res = res.left
      if res:
        return res
    res = node.parent
    while res and res.key < node.key:
      res = res.parent
    return res
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

# Get a reference to the node whose key is 9
# Find the in order successor of test

test = bst.getNodeByKey(9)
succ = bst.find_in_order_successor(test) # 11
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")
test = bst.getNodeByKey(5)
succ = bst.find_in_order_successor(test) # 9
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")
test = bst.getNodeByKey(25)
succ = bst.find_in_order_successor(test) # null
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")
test = bst.getNodeByKey(14)
succ = bst.find_in_order_successor(test) # 20
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")

# Print the key of the successor node

  def find_in_order_successor(self, inputNode):
    '''
    9 11: in right subtree, find the smallest (most left and down)
    14 20: if no right subtree, then go up (if parent exists) until you find element bigger than you
    25 null: no right subtree, up to root, nothing bigger
    12: 14
    
    cur : 20
    res : null
    '''
    cur=inputNode.right
    res=None
    while cur:
      res,cur=cur,cur.left
    if not res:
      cur=inputNode.parent
      while cur:
        if cur.key>inputNode.key:
          res=cur
          break
        cur=cur.parent
    return res