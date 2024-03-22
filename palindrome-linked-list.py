# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 2 1
    s
        f
1 2 3 3 2 1        
    s
        f
1. for odd numbered, slow is in the mid
2. for even numbered, slow is end of the list. 
so for both, s.next is the beginning of the 2nd half!

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
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=''
        while head:
            s+=str(head.val)
            head=head.next
        return s==s[::-1]