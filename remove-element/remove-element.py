class Solution:
    '''
    nums = [2,2,3,3], val = 3
                   i
                j
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        return j
