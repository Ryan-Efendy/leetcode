import heapq

class SummaryRanges:
    def __init__(self):
        self.heap = []
        self.seen = set()

    def addNum(self, val):
        if val in self.seen: return

        self.seen.add(val)
        heapq.heappush(self.heap, [val, val])

    def getIntervals(self):
        stack = []

        while self.heap:
            cur = heapq.heappop(self.heap)
            if stack and cur[0] <= stack[-1][1] + 1:
                stack[-1][1] = max(stack[-1][1], cur[1])
            else:                                    
                stack.append(cur)

        self.heap = stack
        return self.heap