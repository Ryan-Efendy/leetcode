class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        j, mx = None, -math.inf
        for i, num in enumerate(nums):
            if num > mx:
                mx, j = num, i
        
        for num in nums:
            if num != mx and num*2 > mx: return -1
        
        return j
