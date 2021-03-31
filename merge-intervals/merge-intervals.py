class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            # check if prev end >= curr start
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res