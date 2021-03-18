class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval:interval[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if res and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res
                