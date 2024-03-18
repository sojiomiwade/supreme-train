# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
0 1 2 ... 3 4
1,2,3,...-3,4
1 3 6 ... 3 7

have[3] is the head, and it will point to the next of this 3 if 3 exists. 
    otherwise have[3]=this node
then just return the head. 
can use a prehead and can do everything in one iteration

     d 0  1 2
lis  0 1 -1 2
psum 0 1  0 2
     .------>
            c  
have {0:0, 1:1, }
0  1 3 2 -3 -2  5  5 -5 1
0  1 4 6  3  1  6 11  6 7
   ----------c-->
   n          
0  1 2 3. 4. 5. 7  8
                      c
lis  d 01 02
psum 0  0  0 
           c
     ------>   
have {0:d}
'''
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        have={}
        cur=dummy=ListNode(0,head)
        psum=0
        while cur:
            psum+=cur.val
            node=have.get(psum,cur)
            while psum in have:
                have.popitem()
            have[psum]=node
            node.next=cur=cur.next
        return dummy.next