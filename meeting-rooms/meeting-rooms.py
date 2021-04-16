class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        intervals = [[1,3],[4,6],[8,10],[9,18]]
        
               ✅            ❌         
          A-A-A         A-A-A      
                B-B-B     B-B-B-B-B-B-B-B-B-B  
        -----------------------------------------
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0  
            
        1. Sort
        2. Check overlap: meetingA.end > meetingB.start
           A     B    
        [[1,3],[4,6],[8,10],[9,18]]
        
                 A     B    
        [[1,3],[4,6],[8,10],[9,18]]
        
                        A     B    
        [[1,3],[4,6],[8,10],[9,18]]
        '''
        intervals.sort(key=lambda x:x[0])
        for i in range(1, len(intervals)):
            meetingA = intervals[i-1]
            meetingB = intervals[i]
            if meetingA[1] > meetingB[0]:
                return False
        return True