"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hasht = {}
        #headc = Node(None)
        current = head
        while current:
            hasht[current] = Node(current.val)
            current = current.next
        
        current = head

        while current:
            copy = hasht[current]
            if current.next:
                copy.next = hasht[current.next]
            if current.random:
                copy.random = hasht[current.random]
            current = current.next
        
        return hasht[head]


        

            
        