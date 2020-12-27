class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, res = 0, 0
        while i < len(nums):
            if not nums[i]: i+=1
            j = i
            while j < len(nums):
                if not nums[j]: break
                j+=1
            res = max(res, j-i)
            i = j+1
        return res
                
