class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
                        A      B      C
        intervals = [[0,30],[5,10],[15,20]]
        
         AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        
               BBBBBB     CCCCCC  
        
        |-----|-----|-----|-----|-----|-----|
        0     5    10     15    20    25    30
        
        min_heap = [30] -> [10, 30] -> [20, 30]
                    \U0001f446         \U0001f446          \U0001f446
               push 30     push 10    pop 10, push 20
        '''
        if not intervals: return 0
        
        # sort by start time
        intervals.sort(key=lambda interval: interval[0])
        
        usedRooms = [intervals[0][1]] # end times
        heapq.heapify(usedRooms)
        
        for interval in intervals[1:]:
            # overlap
            if interval[0] < usedRooms[0]:
                heapq.heappush(usedRooms, interval[1])
            else:
                heapq.heappop(usedRooms)
                heapq.heappush(usedRooms, interval[1])
        return len(usedRooms)