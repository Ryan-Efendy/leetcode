class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        https://www.youtube.com/watch?v=cI3ivGemzsg
        
        matrix = [   0  1  2
                 0 [ 1, 5, 9],    k = 8
                 1 [10,11,13],
                 2 [12,13,15]
                 ]
        
        '''
        minHeap = []
        for i, num in enumerate(matrix[0]):
            heappush(minHeap, (num, 0, i)) # num, row, col 

        while minHeap:
            num, row, col = heappop(minHeap)
            k -= 1
            if k == 0:
                return num

            if row + 1 < len(matrix[i]):
                heappush(minHeap, (matrix[row+1][col], row+1, col))
        return -1