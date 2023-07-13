class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode):
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        #Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_pointer = slow.next
        previous = None
        spare = None
        slow.next = None

        #Reverse second half
        while right_pointer:
            spare = right_pointer.next
            right_pointer.next = previous
            previous = right_pointer
            right_pointer = spare

        left_pointer = head
        right_pointer = previous
        spare_left = None
        spare_right = None

        #Combine 1st and 2nd half
        while right_pointer:
            spare_left = left_pointer.next
            spare_right = right_pointer.next
            left_pointer.next = right_pointer
            right_pointer.next = spare_left
            left_pointer = spare_left
            right_pointer = spare_right



