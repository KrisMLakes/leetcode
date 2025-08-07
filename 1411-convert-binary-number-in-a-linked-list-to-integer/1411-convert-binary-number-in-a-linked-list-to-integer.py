# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        i = 0
        while current:
            i = i + 1
            current = current.next
        val1 = 0
        while head:
            i = i-1
            val1 = val1 + head.val*(2**i)
            
            #princt ()
            head = head.next
        return val1
        