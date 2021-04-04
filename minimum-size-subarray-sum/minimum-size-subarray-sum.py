class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        res = math.inf
        total = 0
        while j < len(nums):
            total += nums[j]
            
            while total >= target:
                res = min(res, j - i + 1)
                total -= nums[i]
                i += 1
            
            j += 1
        return 0 if res == math.inf else res