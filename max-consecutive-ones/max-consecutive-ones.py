class Solution:
    '''
    [1,1,0,1,1,1]
     
    [1,1,1,1,1]
    '''
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, tmp, res = 0, 0, 0
        while i < len(nums):
            if nums[i] == 0:
                tmp = 0
            else:
                tmp += 1
            res = max(res, tmp)
            i += 1
        return res
