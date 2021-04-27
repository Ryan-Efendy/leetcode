# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi)//2
            res =  guess(mid)
            if res == 0 :
                return mid
            elif res == -1:
                hi = mid - 1
            else:
                lo = mid + 1