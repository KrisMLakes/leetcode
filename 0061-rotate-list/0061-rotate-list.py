# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = 1
        rotated = {}
        if head is None:
            return head
        while current.next:
            count +=1
            current = current.next
        

        k = k % count
        if k == 0:
            return head

        current.next = head
        n = count - k +1
        print (n)

        while n != 0:
            current = current.next
            n -=1
        head = current
        

        while count !=1:
            current = current.next
            count -=1
        current.next = None
        return head

        
        

        