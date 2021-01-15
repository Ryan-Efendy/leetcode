class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        if len(nums1) > len(nums2):
            s = set(nums1)
            for num in nums2:
                if num in s:
                   res.add(num) 
        else:
            s = set(nums2)
            for num in nums1:
                if num in s:
                   res.add(num)
        
        return list(res)
            
        
                
