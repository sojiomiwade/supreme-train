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
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr = head, head.next, 
        while curr:
            temp = curr.next # x
            curr.next = prev # 1
            prev = curr
            curr = temp
        head.next = None
        return prev
n = 5
sol = Solution()
for val in range(n):
    sol.append_to_tail(val + 1)
print(sol.as_list(sol.dummyhead))
node = sol.reverseList(sol.dummyhead.next)
print(sol.as_list(node))
