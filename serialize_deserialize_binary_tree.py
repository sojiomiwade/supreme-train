'''
        5
    2      3
  1  n   9   n
 n x    n n
ans:521#x#39###
        ^ 
deserialize from ans:
        5
     2
  1

this is it:
deser(arr)
    x=arr.popleft()
    if x=='#'
        return None
    root=node()
    root.left=deser(arr)
    root.right=deser(arr)
    return root
if arr
    return deser(arr)
return None

root=cur=null
as long as next != #, 
    cur=node(next) 
    if prev prev.left=cur
    prev=cur
otherwise 
    prev.right=next.next


not a # cur.left gets node(next) and cur = cur.left,
if # cur.left=null and stop, and cur.right=next (or null)
rinse and repeat
return root
'''
class Node:
    ...

def deser(arr) -> Node:
    
