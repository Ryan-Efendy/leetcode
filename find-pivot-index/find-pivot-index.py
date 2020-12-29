class Solution:
    '''
    nums = [1,7,3,6,5,6]
    pref = [1,8,11,17,22,28]
            &
    '''
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1 
        if len(nums) == 1: return 0
        if len(nums) == 2: return -1
       
        prefix = [None] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            
        if prefix[len(nums)-1] - prefix[0] == 0: return 0
        
        for i in range(1, len(prefix)):
            if prefix[i-1] == prefix[len(prefix)-1] - prefix[i]:
                return i
        return -1
