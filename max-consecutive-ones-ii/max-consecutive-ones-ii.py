class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i, j, k = 0, 0, 1
        while j < len(nums):
            if not nums[j]: k -= 1
            j += 1
            while k < 0:
                if not nums[i]: k += 1
                i += 1
            res = max(res, j-i)
        return res
