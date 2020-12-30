class Solution:
    '''
    [0,1,2,3,4,0,2,1,3,1]
                       i
             j
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return j+1
