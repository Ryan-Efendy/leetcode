class Solution:
    '''
    [10, 5, 2, 6]
      i    
         j  
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = j = res = 0
        product = 1
        while j < len(nums):
            product *= nums[j]
            while i < j and product >= k:
                product /= nums[i]
                i += 1
            if product < k:
                res = res + j - i + 1
            j += 1
        return res
                
                
        
