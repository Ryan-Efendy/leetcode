from heapq import *

class MedianFinder:
    '''
        One minheap to store low values and second maxheap to store max values, we keep track and update median every time after insertion
		TIME COMPLEXITY : O(logN) | SPACE COMPLEXITY : O(N)
        
        Adding number 41
        MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
        MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
        Median is 41
        =======================
        Adding number 35
        MaxHeap lo: [35]          // max heap stores smaller half of nums
        MinHeap hi: [41]          // min heap stores bigger half of nums
        Median is 38
        =======================
        Adding number 62
        MaxHeap lo: [41, 35]
        MinHeap hi: [62]
        Median is 41
        =======================
        Adding number 4
        MaxHeap lo: [35, 4]
        MinHeap hi: [41, 62]
        Median is 38
        =======================
        Adding number 97
        MaxHeap lo: [41, 35, 4]
        MinHeap hi: [62, 97]
        Median is 41
        =======================
        Adding number 108
        MaxHeap lo: [41, 35, 4]
        MinHeap hi: [62, 97, 108]
        Median is 51.5
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []  # containing first half of numbers
        self.minHeap = []  # containing second half of numbers
        

    def addNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # either both the heaps will have equal number of elements or max-heap will have one
        # more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            
    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
        # we have even number of elements, take the average of middle two elements
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        # because max-heap will have one more element than the min-heap
        return -self.maxHeap[0] / 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()