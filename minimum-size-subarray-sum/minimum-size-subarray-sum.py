class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j = 0, 0
        window_sum, min_len = 0, math.inf
        for j in range(len(nums)):
            window_sum += nums[j]
            while window_sum >= s:
                min_len = min(min_len, j - i + 1)
                window_sum -= nums[i]
                i += 1
​
        return 0 if min_len == math.inf else min_len
