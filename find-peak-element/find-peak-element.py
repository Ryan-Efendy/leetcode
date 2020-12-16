class Solution:
    '''
            0,1,2,3,4,5,6,7,8,9,10
    nums = [1,2,3,4,5,6,7,8,1,2,3]
            l         m
                                r
    
            0,1,2,3,4,5,6
    nums = [1,2,1,3,5,6,4]
            l 
                  m   r    
                  
            0,1,2,3,4,5,6,7      
    nums = [1,2,3,4,5,6,7,8]
            l     m
                          r
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        def condition(value):
            return nums[value] > nums[value+1]              
        
        if len(nums) == 1: return 0
​
        l, r = 0, len(nums)-1
        
        while l < r:
            m = l + (r-l)//2
            if condition(m):
                r = m
            else:
                l = m + 1
        return l
