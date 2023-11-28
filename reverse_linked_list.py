# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val: Optional[int]=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        self.tail = self.dummyhead = ListNode(None)

    def append_to_tail(self, val: int) -> ListNode:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        return self.tail

    def as_list(self, node: Optional[ListNode]) -> List[int]:
        res, curr = [], node
        while curr:
            res += [curr.val]
            curr = curr.next
        return res

    '''
    1<-2<-3<-4<-5
    p  c  t
                c    
                 t
    for each node as long as curr.next is defined
        save curr's next's next as temp             
        set curr.next to curr
        advance curr 
    finally set dh.next.next = null    

1 2 3
  p c
    1<-2<-3  x
    p  c  t
       p  c  t
          p  c

   <-1<-2<-3
           p
             c   
             t
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next # x
            curr.next = prev # 1
            prev = curr
            curr = temp
        return prev

    def rl_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rr(curr: Optional[ListNode]) -> Optional[ListNode]:
            if not curr or not curr.next:
                return curr
            head = rr(curr.next)
            curr.next.next = curr
            return head

        return rr(head)

n = 5
sol = Solution()
for val in range(n):
    sol.append_to_tail(val + 1)
print(sol.as_list(sol.dummyhead))
node = sol.reverseList(sol.dummyhead.next)
print(sol.as_list(node))
'''
reverse a linked list
p a b 
n<0 1 2 3
  p a
3 2 1 0


    b
n<2 n
  p a
'''
def reverse_ll(lis):
    p=None
    a=lis
    while a:
        b=a.next
        a.next=p
        p,a=a,b
    return p

class Node:
    def __init__(self,val,next=None) -> None:
        self.val=val
        self.next=next

lis=Node(1,Node(2,Node(3)))
rlis=reverse_ll(lis)
print(rlis.val) # 3
print(rlis.next.val) # 2'''
reverse a linked list recursively
  1 2 3 4 n
  p c n
n<a b 

n1
    12
        23
            34
                4n

set cur to point to prev
next = call recursively(cur,next)
next points to curr
'''
class Node:
    def __init__(self,val,next) -> None:
        self.val=val
        self.next=next

def reverse(prev, cur):
    if cur:
        next=cur.next
        cur.next=prev
        return reverse(cur,next)
    return prev

node=Node(1,Node(2,Node(3,Node(4,None))))
print(node.next.val, node.next.next.val) # 2 3
node=reverse(None,node)
print(node.next.val, node.next.next.val) # 3 2