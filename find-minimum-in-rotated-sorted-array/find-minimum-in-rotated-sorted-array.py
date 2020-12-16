class Solution:
    '''
            0 1 2 3 4 
    nums = [3,4,5,1,2]
                  l           
                    r   
            0 1 2 3 4 5 6        
    nums = [4,5,6,7,0,1,2]
                    l 
                    m r
            0  1  2  3   4
    nums = [20,11,13,15,17]
            l  m   
                  r
            0,1
    nums = [2,1]
            l r
    '''
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0: return nums[0]
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
