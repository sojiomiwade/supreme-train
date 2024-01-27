# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        a b c d e
                p c t  
        next point to cur, then call rev on cur.next and its next
        stop when cur.next is null. then return cur
        
        prev,cur=None, starts at null
        then loop on cur=head until cur is none.
            cur
            cur.next=prev
            prev,cur
        return prev

        n<-a  n
           p  c

        n<-a<-b<-c
                 p  c  t 
        '''
        prev,cur=None,head
        while cur:
            temp=cur.next
            cur.next=prev
            prev,cur=cur,temp
        return prev
