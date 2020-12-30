class Solution:
    '''
    [1,0,0,3,12]
           i
       j
    
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums):
            while i < len(nums) and not nums[i]:
                i += 1
            while j < i and nums[j]:
                j += 1
            if i < len(nums) and j < i and nums[i] and not nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1
