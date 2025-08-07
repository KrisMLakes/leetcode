# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = head
        #reversed = head
        prev = None
        #current = head

        fast = head
        current = head
        while fast and fast.next:
            current = current.next
            fast = fast.next.next
        
        #current = slow

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        while prev:
            if prev.val != dummy.val:
                return False
            prev = prev.next
            dummy = dummy.next
        return True
