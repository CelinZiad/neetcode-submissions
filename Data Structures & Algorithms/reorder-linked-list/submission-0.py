# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        second = head.next
        while (second is not None and second.next is not None):
            first = first.next
            second = second.next.next

        second = first.next
        first.next = None
        
        current = second
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        first = head
        second = prev

        while (second is not None):
            temp_next_first = first.next
            temp_next_second = second.next
            first.next = second
            second.next = temp_next_first
            first = temp_next_first
            second = temp_next_second
        