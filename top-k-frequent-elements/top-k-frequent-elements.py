class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [x[0] for x in collections.Counter(nums).most_common(k)]
        
        counter = collections.Counter(nums)
        minHeap = []
        for num, freq in counter.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        while minHeap:
            res.insert(0, heapq.heappop(minHeap)[1])
        return res