class Solution:
    '''
    [1, 8, 23, 24, 33, 34, 54, 75] k = 60
           i
                        j
    '''
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2: return -1
        nums.sort()
        res = -1
        i, j = 0, len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s < k:
                if s > res: res = s
                i += 1
            else:
                j -= 1
        return res
        
