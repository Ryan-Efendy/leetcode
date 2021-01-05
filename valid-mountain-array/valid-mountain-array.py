class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        i = 0
        while i < len(nums):
            if i == 0 and nums[i] >= nums[i+1]:
                break
            elif i != 0 and nums[i-1] >= nums[i]:
                break
            i += 1
            
        if i == 0 or i == len(nums): return False
            
        while i < len(nums):
            if nums[i-1] <= nums[i]: return False
            i += 1
            
        return True
            
