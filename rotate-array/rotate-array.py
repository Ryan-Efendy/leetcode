class Solution:
    """
    nums = [1,2,3,4,5,6,7] k = 3
    [1,2,3,1,5,6,7]
    [1,2,3,1,5,6,4]
    [1,2,7,1,5,6,4]
    [1,2,7,1,5,3,4]
    [1,6,7,1,5,3,4]
    [1,6,7,1,2,3,4]
    [5,6,7,1,2,3,4]
    
    
    nums = [1,2,3,4,5,6,7] k = 3
    [7,6,5,4,3,2,1]
    [5,6,7,1,2,3,4]
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return nums
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, (k%len(nums))-1)
        self.reverse(nums, k%len(nums), len(nums)-1)
        
    def reverse(self, lst, i, j):
        """
        Do not return anything, modify s in-place instead.
        """
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
​
