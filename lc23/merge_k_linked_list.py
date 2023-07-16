# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged = self.mergeTwoLists(l1, l2)
                merged_list.append(merged)
            lists = merged_list
        return lists[0]

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
