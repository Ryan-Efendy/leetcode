class Solution:
    '''
    [1,1,1,2,2,3]
           i
         j
    
    [0,0,1,1,1,1,2,3,3]
     i
     j
     
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 2
        while i < len(nums):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1
            i +=1 
        return j
