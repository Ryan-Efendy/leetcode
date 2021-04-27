# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        1 -› n
        0000000111111
        
        FFFFFTT 
        L  M  R - if mid is False search right

        FFFTTTT  
        L  M  R - if mid is True check if it's the first one else search left
        '''
        l, r = 0, n
        while l < r:
            m = l + (r-l)//2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l