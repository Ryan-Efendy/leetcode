class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        minHeap = []
        counter = collections.Counter(arr)
        
        for num, freq in counter.items():
            heapq.heappush(minHeap, (freq, num))
            
        for _ in range(k):
            freq, num = heapq.heappop(minHeap)
            if freq > 1:
                heapq.heappush(minHeap, (freq-1, num))
        
        return len(minHeap)