# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        l3 = head
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            sum1 = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum1//10
            l3.next = ListNode(sum1%10)
            l3 = l3.next


            l1 = l1.next if l1 else None
            l2=l2.next if l2 else None
            #l3.val=reminder
        #print(l3.val)
           # l1
        return head.next
        