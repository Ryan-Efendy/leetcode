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
        preSum = [0] * (len(nums)+1)
        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + nums[i]
        d = {}
        res = 0
        for i in range(len(preSum)):
            if preSum[i]-k in d:
                res = max(res, i - d[preSum[i]-k])
            if preSum[i] in d:
                d[preSum[i]] = min(d[preSum[i]], i)
            else:
                d[preSum[i]] = i
        return res
