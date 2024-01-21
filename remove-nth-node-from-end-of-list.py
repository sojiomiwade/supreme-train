# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
'''
    p
0 1 2 3 4
1 2 3 4 5
      2 1
m=5
5-2=3
remove 3+1 node => idx from 0 is 3 => prev is 2
pidx=m-n-1

n 1

pidx=1-1=0 correct, assuming m=number of nodes without dh
pidx=1-1-1=-1
with dh, idx we want is now m-n !!!!!

      should be here
      |
        p    
(0) 1 2 3 4 5
n=2 => remove 4
m=5, pidx=5-2=3
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dh=ListNode(None,head)
        m=0
        while head:
            head=head.next
            m+=1
        pidx=m-n
        prev=dh
        for idx in range(pidx):
            prev=prev.next
        prev.next=prev.next.next
        return dh.next