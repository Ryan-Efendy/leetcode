class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        1,0,0,1,1,0   k=2
        i
                j

        maxLen = 5
        counter = 2
        
        0,0,1,1,0,0,1,1  k=3
            i
                      j

        maxLen = 7
        counter = 3
        '''
        i, count, res = 0, 0, 0
        
        for j, num in enumerate(nums):
            if not num:
                count += 1
                
            while count > k:
                if not nums[i]:
                    count -= 1
                i += 1
            
            res = max(res, j-i+1)
        return res