class Solution:
    '''
    nums = [4, 5, 0,-2,-3, 1], k = 5
  preSum = [4, 4, 4, 2, 4, 0]
  
  {
    0: 1,
    4: 1,
    
  }
    
    '''
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))
        
        res = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(prefix)):
            if prefix[i]%k in d:
                res += d[prefix[i]%k]
            d[prefix[i]%k] += 1
        return res
