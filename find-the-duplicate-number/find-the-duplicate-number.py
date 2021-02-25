class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num-1] < 0:
                return abs_num
            nums[abs_num-1] *= -1
        