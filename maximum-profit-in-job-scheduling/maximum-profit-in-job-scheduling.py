class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        DP -  If we assume we only look at the last job when having sorted the jobs by endTime
        then either (1) we pick it or (2) we don't. 
        
        1. sort by endTime
        2. recusion formula: 
            dp[i] = max proft at ith job
            dp[i] = max(dp[i-1], dp[j] + profit) where j is the last job whose endTime <= start
            
        https://www.youtube.com/watch?v=XJp-aOn35y4
        https://www.youtube.com/watch?v=iIX1YvbLbvc
        '''
        # sort by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        endTimes = [e for s,e,p in jobs]

        # can do n+1 instead of just n
        dp = [0] * len(jobs)
        dp[0] = jobs[0][2] # the max profit for first job is scheduling that first job
        for i in range(1, len(jobs)):
            start = jobs[i][0]
            end = jobs[i][1]
            profit = jobs[i][2]

            # 1. either not schedule current job
            dp[i] = dp[i-1]

            # 2. or schedule current job
            # find first job who's endTime <= startTime
            # endTimes=[10,20,30], startTime=15 bisect_right(endTimes, startTime) => 1 
            # bisect_right b/c if there's multiple startTime i.e. 0,1,2,3,4,5,5,5 we're going to insert at 4
            # we want to insert on the right side
            idx = bisect.bisect_right(endTimes, start) - 1 # binarySearch > linearSearch
            # if idx < 0 there's nothing in the dp (index out of bound) set to 0
            dp[i] = max(dp[i], (dp[idx] if idx >= 0 else 0) + profit)

        return dp[-1]