class Solution:
    # flip the least significant bit
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1 
            count += 1
        return count
    
    # count each bit O(32) ~ O(1)
    def hammingWeight2(self, n: int) -> int:
        count = 0
        mask = 1
        while n:
            count += n & mask
            n >>= 1
        return count
        
            