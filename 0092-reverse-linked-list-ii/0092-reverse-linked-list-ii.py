# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        if not head or not head.next:
            return head
        
        for _ in range(left-1):
            prev = prev.next
            
        prev_sublist = None

        
        
        current = prev.next
        tail = current
        i = 0
        for i in range(right-left+1):
                nextNode = current.next
                current.next = prev_sublist
                prev_sublist = current
                current = nextNode

        prev.next = prev_sublist
        tail.next = current
                
        return dummy.next
                

        
            
            