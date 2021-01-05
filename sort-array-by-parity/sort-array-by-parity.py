class Solution:
    """
    [3,1,2,4]
​
    i      j
    """
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return nums
