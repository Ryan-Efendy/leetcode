class Solution:
    '''
    nums = [3,4,7,2,-3,1,4,2] k=7
           [3,7,14,16,13,14,18,20]
              i 
    nums = [1,2,3], k = 3
           [1,3,6]
    nums = [1,1,1], k = 2
           [1,2,3]
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))
        
        res = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(prefix)):
            if prefix[i]-k in d: res += d[prefix[i]-k]
            d[prefix[i]] += 1
        return res
            
                
             
