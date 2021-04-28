class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        '''
                       i                 j[start] >= i[end]?   output
        intervals = [[3,4],[2,3],[1,2]]     2 >= 4 ❌
                             j
                       i
        intervals = [[3,4],[2,3],[1,2]]     1 >= 4 ❌          [-1]
                                   j
                             i
        intervals = [[3,4],[2,3],[1,2]]     3 >= 3 ✅          [-1,0]
                       j         
                                   i
        intervals = [[3,4],[2,3],[1,2]]     3 >= 2 ✅  \
                       j                                [3,4]  min(start1, start2) => [2,3] ✅  
                                   i                    [2,3]
        intervals = [[3,4],[2,3],[1,2]]     2 >= 2 ✅  /       [-1,0,1]
                             j                
                                  
        '''
        def bisect_left(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
        
        res = []
        n = len(intervals)
        # get original index before sort ruins index
        starts = {interval[0]:i for i, interval in enumerate(intervals)} # starts: {3: 0, 2: 1, 1: 2}
        sorted_starts = sorted([interval[0] for interval in intervals]) # [1,2,3]

        for star, end in intervals:
            target = end
            # binary search
            index = bisect_left(sorted_starts, target)
            
            if index == n: # if index is out of bound or greater than sorted_starts[-1]
                res.append(-1)
            else:
                start_point = sorted_starts[index]
                res.append(starts[start_point])

        return res