# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy.next
        prev = None
        val1 = 0
        #val2 = 0
        i = 0
        while i<k and fast.next:
            i = i + 1
            fast = fast.next
        val1 = fast.val
        #print(val1)
        prev = fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        prev.val = slow.val
        #print(slow.val)
        slow.val = val1
        
        return dummy.next




            
        