# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val>list2.val:
                list1,list2=list2,list1
            list1.next=merge(list1.next,list2)
            return list1
        return merge(list1,list2)