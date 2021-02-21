class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.tail = None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.tail = Node(value)
            self.head = self.tail
        else:
            node = Node(value)
            if not self.tail:
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            if not self.head:
                self.head = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = self.head.next
        if not self.tail:
            self.tail = self.head
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()