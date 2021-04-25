class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        n = len(intervals)
        # get original index before sort ruins index
        starts = {interval[0]:i for i, interval in enumerate(intervals)}
        sorted_starts = sorted([interval[0] for interval in intervals])

        for star, end in intervals:
            target = end
            # binary search
            index = bisect.bisect_left(sorted_starts, target)

            if index == n: # if index is out of bound or greater than sorted_starts[-1]
                res.append(-1)
            else:
                start_point = sorted_starts[index]
                res.append(starts[start_point])

        return res