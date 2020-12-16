class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def condition(value):
            return nums[value] >= target
​
        def condition2(value):
            return nums[value] > target
​
        ret = [-1,-1]
        if len(nums) == 0: return ret
​
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return ret
        ret[0] = left
​
        right = len(nums)
        while left < right:
            mid = left + (right-left) // 2
            if condition2(mid):
                right = mid
            else:
                left = mid + 1
        ret[1] = left-1
        return ret
