# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
l2 1 2 3
l1 0     

'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
        next = self.mergeTwoLists(list1.next, list2.next)
        list1.next = list2
        list2.next = next
        return list1