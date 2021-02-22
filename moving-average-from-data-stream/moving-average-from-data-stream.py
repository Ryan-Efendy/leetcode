class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val
        self.q.append(val)
        while len(self.q) > self.size:
            val2 = self.q.popleft()
            self.sum -= val2
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)