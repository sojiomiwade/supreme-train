# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 2 1
    s
        f
actually no need for all that. 
just 
if f doesn't have a next, then prev of slow is tail
and next of slow is next head

1 2 3 3 2 1        
    s
        f
otherwise, slow is tail, and next of slow is next head

1. for odd numbered, slow is in the mid
2. for even numbered, slow is end of the list. 
so for both, s.next is the beginning of the 2nd half!

reverse s.next
now when you iterate, list 2 couod have one fewer & that is ok.

make the number as you go with a string. then check it at the end
1 2 5 4 3 4 5 2 1
          1 2 5 4
s 
        f
4 5 2 1 3 1 2 5 4  
s
         f
          

        h
        l
could also form a number and lg n, check ==> O(n+lgn) and O(1) space!
10(10**5)

1 2 3 2 1
    s
        f
if f doesn't have a next, then prev of slow is tail
and next of slow is next head

1 3 2 3 1        
    s
        f
1 3 1 3        
    s
        f
if fast, then head2 is s.next, otherwise, it is just s

n 3 2 1
p h
otherwise, slow is tail, and next of slow is next head
1 3 3 1        
    t
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def gethead2(head):
            slow=fast=head
            while fast and fast.next:
                slow,fast=slow.next,fast.next.next
            if fast:
                slow=slow.next
            return slow
        '''
          /----\
        1 3   n<-3<-1   n
                    p
                        h2 
                       nh
        h    
        '''
        def reverse(head):
            prev=None
            while head:
                nexthead=head.next
                head.next=prev
                prev,head=head,nexthead
            return prev

        head2=gethead2(head)
        head2=reverse(head2)
        while head2:
            if head2.val!=head.val:
                return False
            head,head2=head.next,head2.next
        return True


