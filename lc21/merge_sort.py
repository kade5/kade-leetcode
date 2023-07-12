# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        merged_head = None
        sorted = None
        l1 = list1
        l2 = list2
        previous = None
        
        while l1 or l2:
            if sorted is None:
                sorted = ListNode()
                merged_head = sorted

            if l1 and (l2 is None or l1.val <= l2.val):
                sorted.val = l1.val
                if previous:
                    previous.next = sorted
                previous = sorted
                sorted = ListNode()
                l1 = l1.next
            else:
                sorted.val = l2.val
                if previous:
                    previous.next = sorted
                previous = sorted
                sorted = ListNode()
                l2 = l2.next



        return merged_head
