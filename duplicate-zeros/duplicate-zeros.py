class Solution:
    """
    [1,0,2,3,0,4,5,0]
         i
    
    """
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        def shift(nums, i):
            n = len(nums)-1
            while n > i:
                nums[n] = nums[n-1]
                n -= 1
            nums[n] = 0
        
        i = 0
        while i < len(nums):
            if i != 0 and nums[i-1] == 0:
                shift(nums, i)
                i += 2
            else:
                i += 1
​
