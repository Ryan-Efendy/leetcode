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
        preSum = list(accumulate(nums))
        d = {0: -1}
        res = 0
        for i in range(len(preSum)):
            if preSum[i]-k in d:
                res = max(res, i - d[preSum[i]-k])
            if preSum[i] not in d:
                d[preSum[i]] = i
        return res
