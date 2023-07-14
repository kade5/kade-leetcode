# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        right_pointer = head
        left_pointer = ListNode(0, head)
        counter = 0

        while right_pointer:
            right_pointer = right_pointer.next
            if counter >= n:
                left_pointer = left_pointer.next
            counter += 1

        if counter - n == 0:
            return head.next
        
        left_pointer.next = left_pointer.next.next
        return head
