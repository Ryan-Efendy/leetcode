class KthLargest:
    '''
    https://www.youtube.com/watch?v=aaWU4Bq1X-c
    https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/232147/Simplest-Python-MinHeap-Solution
    
    If you want to find Kth largest element maintain MinHeap of K elements similarlary if you want Kth smallest element maintain MaxHeap of k elements.
    The element of the heap would be the Kth element.
    '''

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        # if heap grows bigger then k remove elements
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)