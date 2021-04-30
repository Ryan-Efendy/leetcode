class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        nums = [1,2,5,9], threshold = 6
        
        divisor  sum         round up i.e. 4.5 => 5                                6
        1        17  =  (1/1) + (2/1) + (5/1) + (9/1) => 1 + 2 + 5 + 9 = 17 <= threshold? ❌
        2        10  =  (1/2) + (2/2) + (5/2) + (9/2) => 1 + 1 + 3 + 5 = 10 <= threshold? ❌
        3         7  =  (1/3) + (2/3) + (5/3) + (9/3) => 1 + 1 + 2 + 3 = 7  <= threshold? ❌
        4         7  =  (1/4) + (2/4) + (5/4) + (9/4) => 1 + 1 + 2 + 3 = 7  <= threshold? ❌
        5         5  =  (1/5) + (2/5) + (5/5) + (9/5) => 1 + 1 + 1 + 2 = 5  <= threshold? ✅
        .
        .
        9         3  =  (1/9) + (2/9) + (5/9) + (9/9) => 1 + 1 + 1 + 1 = 4  <= threshold? ✅
        Output: 5 
        '''
        def isDivisorLessThanThreshold(divisor: int) -> bool:
            return sum(math.ceil(num/divisor) for num in nums) <= threshold

        # find lower & upper bound of binarySearch
        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2

            if isDivisorLessThanThreshold(mid):
                right = mid # b/c mid is valid need to be considered still
            else:
                left = mid + 1
        return left