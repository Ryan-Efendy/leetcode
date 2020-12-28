class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def getKOddNumbers(k):
            i, j = 0, 0
            max_len = 0
            while j < len(nums):
                if nums[j] % 2 == 1: k -= 1
                j += 1
                while k < 0:
                    if nums[i] % 2 == 1: k += 1
                    i += 1
                max_len += j-i
            return max_len
        return getKOddNumbers(k) - getKOddNumbers(k-1)
