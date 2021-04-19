class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''        
        intervals = [[1,4],[3,6],[3,7],[2,8]]
        1. sort by (a) start asc then by (b) end desc \U0001f449 [[2,8],[1,4],[3,7],[3,6]]
            a. Interval [a,b) is covered by interval [c,d) if and only if c <= a
            b. and b <= d.
        2. keep track of max_end
        '''
        intervals.sort(key=lambda interval:(interval[0], -interval[1]))
        removed = 0
        max_end = 0

        for s, e in intervals:
            if e <= max_end:
                removed += 1

            max_end = max(max_end, e)

        return len(intervals) - removed