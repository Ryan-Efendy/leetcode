class MyCircularQueue:
    def __init__(self, k: int):
        self.buffer = [None] * k
        self.size = 0
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        if self.isEmpty():
            self.buffer[0] = value
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % len(self.buffer)
            self.buffer[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % len(self.buffer)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.buffer[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.buffer[self.tail]
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.buffer)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()