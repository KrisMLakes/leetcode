class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:  # should be index >= self.size
            return -1

        current = self.head  # use a temporary pointer
        for _ in range(index):
            current = current.next
        return current.val
            

        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1
        #print(self.head.val)

    def addAtTail(self, val: int) -> None:
        if self.size ==0:
            self.head = Node(val)
            self.size = self.size + 1
            return
        current = self.head
        for i in range(self.size-1):
            current = current.next
        current.next = Node(val)
        self.size = self.size + 1
        #print(current.next.val)

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
           # print(index)
            current = self.head
            for _ in range(index - 1):
                current = current.next
           # print(current.next.val, current.next.next.val)
            current.next = current.next.next
        current2 = self.head
        #while current2:
        #    print(current2.val)
        #    current2 = current2.next
        self.size -= 1      
        print(self.size)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)