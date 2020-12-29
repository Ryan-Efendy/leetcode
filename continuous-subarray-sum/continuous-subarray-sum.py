class Solution:
    '''
    Input: [23, 2, 4, 6, 7],  k=6
   preSum: [5 , 1, 5, 5, 0]
                   ^
   {
     5: 1,
     1: 1,
     
   }
   
   nums[i,j] = nums[j] - nums[i-1]
               29 - 23 = 6
               
               
    Input = [23, 2, 6, 4, 7],  k=6
   preSum = [23,25,31,35,42]
   
   {
     5: 1,
     1: 1
     
   }
​
    '''
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # edge case
        if len(nums) < 2: return False
        # edge cases
        for i in range(len(nums)-1):
            if not nums[i] and not nums[i+1]: return True
        
        prefix = [None] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            if k:
                prefix[i] %= k
        
        res = 0
        d = {0: -1}
        for i in range(len(prefix)):
            if prefix[i] in d:
                if i - d[prefix[i]] > 1: return True
            else:
                d[prefix[i]] = i
        return False
​
        
