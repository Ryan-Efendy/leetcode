class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res = 0
        # edge case negative intervals i.e. [-100,-2]
        pre_end = -math.inf

        for start, end in intervals:
            if start < pre_end:
                res += 1
            else:
                pre_end = end

        return res