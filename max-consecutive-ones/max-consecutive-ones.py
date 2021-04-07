class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        1,1,0,1,1,1
         ^
        counter = 1
        maxLen = 2
        '''
        count, res = 0, 0
        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            
            res = max(res, count)
        return res