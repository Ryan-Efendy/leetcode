class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
                       A     B     C       D
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        
                AAA   \U0001f448\U0001f3fc ❗
                 BBBBBB \U0001f448\U0001f3fc ❗ 
                         CCC
                                  DDDD
                |-----|-----|-----|-----|
                0     5    10     15    20  
        
        1. sort
        2. merge intervals
                            \U0001f447    
        intervals =        [[2,6],[8,10],[15,18]]
        merged_intervals = [[1,3]]
                               \U0001f446
        '''
        # sort by start time
        intervals.sort(key=lambda interval: interval[0]) 
        
        merged_intervals = [intervals[0]]
        
        for interval in intervals:
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)
        
        return merged_intervals
                
        
        