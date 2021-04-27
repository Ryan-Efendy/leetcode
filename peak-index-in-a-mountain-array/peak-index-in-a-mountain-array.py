class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        '''
          /\
         /  \ 
        /    \
        0123456
           \U0001f446 
        0001111
        f(i) = arr[i] > arr[i+1]
        '''
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m
        return l