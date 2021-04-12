class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        def maxSubArrayLen(target: int, nums: List[int]) -> int:
            i, j, res, sum = 0, 0, -1, 0
            while j < len(nums):
                sum += nums[j] # grow

                while sum > target and i <= j: # condition
                    sum -= nums[i]
                    i += 1 # shrink

                if sum == target:
                    res = max(res, j - i + 1)
                j += 1
            return 0 if res == math.inf else res

        max_len =  maxSubArrayLen(target, nums)
        return len(nums) - max_len if max_len != -1 else -1