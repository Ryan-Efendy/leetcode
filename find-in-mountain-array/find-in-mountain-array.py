# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        '''
           /\          
    ✅    /   \
    \U0001f449   /     \  \U0001f448 
       /        \
        '''
        def peakIndexInMountainArray(mountain_arr: 'MountainArray') -> int:
            l, r = 0, mountain_arr.length()-1
            while l < r:
                m = l + (r-l)//2
                if mountain_arr.get(m) < mountain_arr.get(m+1):
                    l = m + 1
                else:
                    r = m
            return l
        
        def orderAgnosticBinarySearch(mountain_arr, l, r, target):
            isAscending = mountain_arr.get(l) < mountain_arr.get(r)
            while l < r:
                mid = (l + r)//2
                if isAscending:
                    if mountain_arr.get(mid) < target:
                        l = mid + 1
                    else:
                        r = mid
                # descending
                else:  
                    if mountain_arr.get(mid) > target:
                        l = mid + 1
                    else:
                        r = mid

            return l if mountain_arr.get(l) == target else -1
        
        peak = peakIndexInMountainArray(mountain_arr)
        
        res = orderAgnosticBinarySearch(mountain_arr, 0, peak, target)
        if res != -1:
            return res
        
        res = orderAgnosticBinarySearch(mountain_arr, peak+1, mountain_arr.length()-1, target)
        if res != -1:
            return res
        return res
        