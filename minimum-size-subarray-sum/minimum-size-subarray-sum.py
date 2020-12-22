class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_len, window_sum = math.inf, 0
        i, j = 0, 0
        while j < len(nums):
            window_sum += nums[j]
            j += 1
            while window_sum >= s:
                min_len = min(min_len, j-i)
                window_sum -= nums[i]
                i += 1
        return min_len if min_len != math.inf else 0
