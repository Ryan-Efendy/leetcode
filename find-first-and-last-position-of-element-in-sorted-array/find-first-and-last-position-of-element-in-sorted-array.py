class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        bisect_left & bisect_right
        '''
        def bisect_left(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if l < len(nums) and nums[l] == target else -1
        
        def bisect_right(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                m = l + (r-l)//2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m
            return l-1 if l-1 < len(nums) and nums[l-1] == target else -1

        if len(nums) == 0: return [-1, -1]
        return [bisect_left(nums, target), bisect_right(nums, target)]