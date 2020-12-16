class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] == nums[r]:
                if (r != 0 and nums[r] >= nums[r-1]):
                    r -= 1
                else:
                    return nums[r]
            elif nums[m] > nums[r]:
                l = m + 1
            else:    
                r = m
        return nums[l]
