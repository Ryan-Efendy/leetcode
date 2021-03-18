class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count, mask = 0, 1
        n = x ^ y
        while n:
            count += n & mask
            n >>= 1
        return count