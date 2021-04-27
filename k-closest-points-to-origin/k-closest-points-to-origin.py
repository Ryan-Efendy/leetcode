class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sort O(NlogN)
        # points.sort(key = lambda P: P[0]**2 + P[1]**2)
        # return points[:k]
    
        # Divide and Conquer -> selection sort O(N)
        
        # MaxHeap O(NlogK)
        maxheap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(maxheap, (-dist, point))
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return [tuple[1] for tuple in maxheap]