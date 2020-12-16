class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False
        l, n = 0, len(nums)
        r = n-1
        rotation = None
        while l < r:
            m = l + (r-l)//2
            if nums[m] == nums[r]:
                if (r != 0 and nums[r] >= nums[r-1]):
                    r -= 1
                else:
                    rotation = r
                    break
            elif nums[m] > nums[r]:
                l = m + 1
            else:    
                r = m
                
        if not rotation:
            rotation = l
            
        l, r = 0, n-1
        while l < r:
            m = l + (r-l)//2
            midPlusRotation = (m + rotation) % n
            if nums[midPlusRotation] >= target:
                r = m
            else:
                l = m + 1
        return nums[(l + rotation) % n] == target
            
