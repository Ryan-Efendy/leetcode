class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        '''
         0,1,2,3
        [0,2,1,0]
         l 
         m r
             
         0,1,2,3,4,5,6,7,8,9,10    
        [0,1,2,3,4,5,6,5,4,3,2]
                     l  
                     m r         
        '''
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l
