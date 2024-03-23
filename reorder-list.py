# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 4
  p s
        f

1 2 3 | 4 5
      | m
    s
          f 
find mid
if fast slow is prev. otherwise prev is just prev

1 5 2 4 3
reverse 2nd list, then splice two lists
lists a and b
splice: a.next=b; b.next=splice(anext,bnext)

n 1 2 3 4 5
    p s
          f

'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def findmidprev(head):
            s=f=head
            prev=None
            while f and f.next:
                prev=s
                s,f=s.next,f.next.next
            return s if f else prev

        '''
        n<3<4<5
              p h hn
        '''
        def reverse(head):
            # n 1 2 3 4
            # p h
            prev=None
            while head:
                headnext=head.next
                head.next=prev
                prev,head=head,headnext
            return prev

        # 2->3->
        def splice(a, b):
            if b:
                anext,bnext=a.next,b.next
                a.next=b
                b.next=splice(anext,bnext)
            return a

        '''
        n 1 2 3    4 5
              p    h2 
        1 2 
        5 4 3
        '''
        prev=findmidprev(head)
        head2,prev.next=prev.next,None
        head2=reverse(head2)
        return splice(head,head2)
        