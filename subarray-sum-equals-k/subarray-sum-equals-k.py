from itertools import accumulate
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] += 1
        presums = list(accumulate(nums))
        res = 0
    
        for presum in presums:
            diff = presum - k
            if diff in d:
                res += d[diff]
            d[presum] += 1
            
        return res