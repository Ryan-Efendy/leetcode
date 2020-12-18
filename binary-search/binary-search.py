class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l+1)//2
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        return l if nums[l] == target else -1
