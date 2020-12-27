class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = nums[0], nums[0]
        for num in nums[1:]:
            local_max = max(local_max+num, num)
            global_max = max(global_max, local_max)
        return global_max
            
