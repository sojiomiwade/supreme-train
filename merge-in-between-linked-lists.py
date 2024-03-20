# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
use a dummy head because head can itself be removed
find prev of va and vb
connect prev of va to list2
list2's last to next of vb
return dummy's next
'''
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # d 0 1 (2) 3 4 (5) 6 7 8
        def find(start: ListNode, idx: int) -> Tuple[ListNode, Optional[ListNode]]:
            prev,ans=None,start
            for _ in range(idx):
                prev=ans
                ans=ans.next
                if not ans:
                    break
            return prev,ans

        INTMAX=2**31-1
        dummy=ListNode(0,list1)
        prevva,_=find(dummy,1+a)
        _,vb=find(prevva,b-a+1)
        lis2last,_=find(list2,INTMAX)

        prevva.next=list2
        lis2last.next=vb.next

        return dummy.next
        