class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Euclidean distance (i.e., sqrt((x1 - x2)^2 + (y1 - y2)^2))
                          |     *
                          |    /|   
                          |  /  |  A      A^2 + B^2 = C^2
              ____________|/____|________
                          |   B
                          |
                          |
                          |  
        apprach 1: sort O(NlogN)                          
        '''
        '''
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:k]
        '''
        '''
        Divide and Conquer -> selection sort + partition O(N)
        '''
        
        '''
        maxheap - get k smallest elements O(nlgk)
        '''
        def getDist(x, y):
            return x**2 + y**2
        
        maxheap = []
        for point in points:
            dist = getDist(point[0], point[1])
            heapq.heappush(maxheap, (-dist, point))
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return [tuple[1] for tuple in maxheap]