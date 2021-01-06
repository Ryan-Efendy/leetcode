class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -math.inf
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2 and num < max1:
                max3 = max2
                max2 = num
            elif num > max3 and num < max2:
                max3 = num
        return max1 if max3 == -math.inf else max3 
        
