class Solution:
    '''
    nums = [1,7,3,6,5,6]
    pref = [1,8,11,17,22,28]
            &
    '''
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1 
        if len(nums) == 1: return 0
        if len(nums) == 2: return -1
        
        totalSum, leftSum, rightSum = sum(nums), 0, 0
        for i, num in enumerate(nums):
            rightSum = totalSum - num - leftSum
            if leftSum == rightSum: return i
            leftSum += num
        return -1
