class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1,-1]
        if len(nums) == 0: return ret
        
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        if nums[l] == target:
            ret[0] = l
        else:
            return ret
        
        l, r = l, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        
        ret[1] = l-1
        return ret
