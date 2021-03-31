class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # 1. add intervals starting before newInteral
        i, n = 0, len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2. merge newInterval w/ any overlapping intevals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i +=1
        res.append(newInterval)
        
        # 3. add the remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res