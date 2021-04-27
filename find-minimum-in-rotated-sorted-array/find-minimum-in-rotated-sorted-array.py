class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        |     /  
        |   /     /
        | /     /  
        |_____________
          3 4 5 1 2
               \U0001f447       \U0001f447  
        nums = [3,4,5,1,2] ... nums[mid] > nums[hi] => min val is on the right 
                    \U0001f446         
               \U0001f447        \U0001f447
        nums = [11,13,15,17] ... nums[mid] < nums[hi] => min val in on the left
                       \U0001f446
        '''
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi)//2 
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]