class Solution:
    '''
    A = [1,0,1,0,1], S = 2
    B = [1,1,2,2,3]
                 ^            
    {
        0: 1,
        1: 2,
        2: 2
        
    }
    res = 4
    ---
    A = [1,0,1,0,1], S = 3
         i j
    {
        0: 3
        1: 2
    }
    res = 6
    '''
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))
        
        res = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(prefix)):
            if prefix[i]-k in d: res += d[prefix[i]-k]
            d[prefix[i]] += 1
        return res
