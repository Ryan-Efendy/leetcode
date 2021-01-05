class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        curr_max = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            tmp_max = nums[i]
            nums[i] = curr_max
            curr_max = max(curr_max, tmp_max)
        nums[-1] = -1
        return nums
            
