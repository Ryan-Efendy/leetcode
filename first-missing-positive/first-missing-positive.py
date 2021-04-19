class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        [1, n] or range(1, n-1)
                       1 2 3
        Input: nums = [1,2,0] already cycle sorted
        Output: 3
                        1  2  3  4      1  2  3  4
        Input: nums = [ 3, 4,-1, 1] -> [1, 4, 3, -1]
        Output: 2
                       1  2  3  4  5      1  2  3  4  5  
        Input: nums = [7, 8, 9,11,12] -> [7, 8, 9,11,12]
        Output: 1
        
        '''
        self.cyclic_sort(nums)
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return len(nums) + 1
        
    def cyclic_sort(self, nums):
        i = 0
        while i < len(nums):
            # only swap 0 < num < n
            if nums[i] > 0 and nums[i] < len(nums):
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]  # swap
                else:
                    i += 1
            else:
                i += 1
        return nums