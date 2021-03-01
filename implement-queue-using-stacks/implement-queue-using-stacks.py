class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushStack = []
        self.popStack = []

    def push(self, x: int) -> None:
        """Push element x to the back of queue."""
        self.pushStack.append(x)

    def pop(self) -> int:
        """Removes the element from in front of queue and returns that element."""
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()

    def peek(self) -> int:
        """Get the front element."""
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1]

    def empty(self) -> bool:
        """Returns whether the queue is empty."""
        return not self.popStack and not self.pushStack
    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()