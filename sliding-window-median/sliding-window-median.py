class Solution:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = [0.0 for x in range(len(nums) - k + 1)]  # init
        for i in range(len(nums)):
            self.add(nums[i])
            self.rebalance()

            if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
                res[i - k + 1] = self.find_median()
                # remove the the element going out of the sliding window
                elementToBeRemoved = nums[i - k + 1]
                self.remove(elementToBeRemoved)
        return res        

    # removes an element from the heap keeping the heap property
    def add(self, num):
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

    def find_median(self):
         # add the median to the the result array
        if len(self.maxHeap) == len(self.minHeap):
            # we have even number of elements, take the average of middle two elements & takes care of overflow
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        else:  # because max-heap will have one more element than the min-heap
            return -self.maxHeap[0] / 1.0

    def remove(self, num):
        # Remove element from heap O(lgn): https://stackoverflow.com/questions/10162679/python-delete-element-from-heap
        if num <= -self.maxHeap[0]:
            self.maxHeap.remove(-num)
            heapq.heapify(self.maxHeap)
        else:
            self.minHeap.remove(num)
            heapq.heapify(self.minHeap)

        self.rebalance()

    def rebalance(self):
        # either both the heaps will have equal number of elements or max-heap will have
        # one more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))