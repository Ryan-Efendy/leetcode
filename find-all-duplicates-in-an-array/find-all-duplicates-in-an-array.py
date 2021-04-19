class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        nums = [4, 3, 2, 7, 8, 2, 3, 1] => Output: [2,3]
                0  1  2  3  4  5  6  7    
        nums = [1, 2, 3, 4, 3, 2, 7, 8]
        '''
        res = []
        self.cyclic_sort(nums)
        for i, num in enumerate(nums):
            if num - 1 != i:
                res.append(num)
        return res

    def cyclic_sort(self, nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1
        return nums