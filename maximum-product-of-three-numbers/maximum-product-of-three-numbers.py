class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -math.inf
        min1 = min2 = math.inf
        
        for num in nums:
            if max1 < num:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2 < num:
                max3 = max2
                max2 = num
            elif max3 < num:
                max3 = num
                
            if min1 > num:
                min2 = min1
                min1 = num
            elif min2 > num:
                min2 = num
            
        product1 = max1 * max2 * max3
        product2 = max1 * min1 * min2
        return product1 if product1 > product2 else product2
               
