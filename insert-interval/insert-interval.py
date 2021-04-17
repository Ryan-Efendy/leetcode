class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        
        res: [[1,5],[6,9]]
        
        1. add non-overlapping intervals to newInterval
        2. merge newInterval w/ overlapping intervals
        3. add remaining non-overlapping intervals
        '''
        res = []
        
        for interval in intervals:
            # 1
            if interval[1] < newInterval[0]:
                res.append(interval)
            # 3        
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = interval
            # 2
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
                    
        res.append(newInterval)
        return res
        
        