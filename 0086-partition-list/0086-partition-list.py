# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less_head = ListNode(0)
        more_head = ListNode(0)
        current = head
        less_tail = less_head
        more_tail = more_head
        while current:

            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                more_tail.next = current
                more_tail = more_tail.next
            current = current.next
        less_tail.next = more_head.next
        more_tail.next = None

        return less_head.next

        