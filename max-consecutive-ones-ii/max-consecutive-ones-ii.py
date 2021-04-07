class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        1,0,1,1,0
                ^
        maxLen 4
        counter = 1
        '''
        i, count, res = 0, 0, 0
        
        for j, num in enumerate(nums):
            if not num:
                count += 1
                
            while count > 1:
                if not nums[i]:
                    count -= 1
                i += 1
            
            res = max(res, j-i+1)
        return res
                