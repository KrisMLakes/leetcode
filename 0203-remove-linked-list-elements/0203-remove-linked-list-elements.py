# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = head
        prev = dummy
        while fast:
            #prev = fast
            if fast.val == val:
                prev.next = fast.next
            else:
                prev = fast
            fast = fast.next
        return dummy.next

        