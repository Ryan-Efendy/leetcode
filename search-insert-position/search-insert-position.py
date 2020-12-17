class Solution:
    '''
     0,1,2,3 4
    [1,3,5,6] target=2
       l           
     m r    
     0,1,2,3 4
    [1,3,5,6] target=7
           l
           m r
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
