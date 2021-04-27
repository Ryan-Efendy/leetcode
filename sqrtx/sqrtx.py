class Solution:
    def mySqrt(self, x: int) -> int:        
        def bisect_right(x: int) -> int:
            lo, hi = 0, x
            while lo < hi:
                mid = lo + (hi-lo)//2
                if mid * mid <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo-1
        
        if x == 0 or x == 1: return x
        return bisect_right(x)