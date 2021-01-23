        if not self.head:
            self.addAtHead(val)
        else:
            dummy = self.head
            while dummy.next:
                dummy = dummy.next
            dummy.next = newTail
​
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        newNode = Node(val)
        if not self.head:
            if index == 0: self.head = newNode
            return
        
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        dummy = self.head
        for _ in range(index-1):
            if dummy.next:
                dummy = dummy.next
            else:
                return
        newNode.next = dummy.next
        dummy.next = newNode
​
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not self.head:
            return
        
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        dummy = self.head
        for _ in range(index-1):
            if dummy.next:
                dummy = dummy.next
            else:
                return
        if dummy.next:
            dummy.next = dummy.next.next
        else:
            dummy.next = None
​
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
​
​
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
