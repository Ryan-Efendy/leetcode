class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(i for i in range(len(nums)+1))
        for num in nums:
            s.remove(num)
        return s.pop()
        
