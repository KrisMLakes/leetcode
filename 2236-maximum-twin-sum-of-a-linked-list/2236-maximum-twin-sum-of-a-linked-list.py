# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        n = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            n = n +1
        prev = slow
        current = slow.next

        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        i = 0
        dummy = head
        ans = 0
        while i < n:
            ans = max(ans, dummy.val+prev.val)
            dummy = dummy.next
            prev = prev.next
            i = i+1
        return ans



        