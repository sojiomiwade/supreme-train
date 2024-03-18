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
two pass solution
first get the have map, then start the prefix sum again, and 
if you see the prefix there, go ahead and point to its next. and set yourself to that node
otherwise cur just get cur.next
0  1 3 2 -3 -2  5  5 -5 1
0    4    3  1    11  6 7
0  1 4 6  3  1  6 11  6 7
0  .------------>.------->
             c
list  0 0 0 n
      c-----> 
have -1 x 0 
    
'''
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        have={}
        psum,cur=0,head
        while cur:
            psum+=cur.val
            have[psum]=cur
            cur=cur.next
        cur,psum=dummy,0
        while cur:
            psum+=cur.val
            if psum in have:
                cur.next=have[psum].next
            cur=cur.next
        return dummy.next
