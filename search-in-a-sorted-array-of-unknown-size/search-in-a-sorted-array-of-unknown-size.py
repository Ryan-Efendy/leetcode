# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        '''
        need to find r, by increasing r exponentially -> while (reader.get(r) < target) r *= 2
        1. find search limits, i.e. left & right boundaries for the search
        2. do binary search in the defined boundaries
        '''
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2
        
        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        # there is no target element
        return -1
        