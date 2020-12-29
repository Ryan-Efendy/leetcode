class Solution:
    '''
    nums = [1,-1, 5,-2, 3], k = 3
  preSum = [0, 1, 0, 5, 3, 6]
  
  {
    0: 0
    1: 1
    5: 3
  }
   
   nums = [-2, -1, 2, 1], k = 1
 preSum = [0,-2,-3,-1,0]
    '''
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        cum_sum, res = 0, 0
        d = {0: -1}
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum-k in d:
                res = max(res, i - d[cum_sum-k])
            if cum_sum not in d: 
                d[cum_sum] = i # only keep the oldest index to have the longest subarray
        return res
