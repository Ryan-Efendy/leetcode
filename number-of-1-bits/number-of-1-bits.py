class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1
        while n:
            count += n & mask
            n >>= 1
        return count
        
            