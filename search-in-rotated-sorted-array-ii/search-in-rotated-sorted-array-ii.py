class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False
        n = len(nums)
        l, r, pivot = 0, n-1, None
        while l < r:
            m = l + (r-l)//2
            if nums[m] == nums[r]:
                # find the minimum value index vs. just minimum value
                if (nums[r] < nums[r-1]):
                    pivot = r
                    break
                r -= 1
            elif nums[m] > nums[r]:
                l = m + 1
            else:    
                r = m
        
        if not pivot:
            pivot = l
        
        l, r = 0, n-1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot
        while l < r:
            m = l + (r-l)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return True if nums[l] == target else False
            
