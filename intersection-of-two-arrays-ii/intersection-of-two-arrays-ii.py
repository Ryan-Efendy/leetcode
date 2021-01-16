class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
            counter = collections.Counter(nums1)
            for num in nums2:
                if counter[num] > 0:
                    res.append(num)
                counter[num] -= 1
            return res
        else:
            counter = collections.Counter(nums2)
            for num in nums1:
                if counter[num] > 0:
                    res.append(num)
                counter[num] -= 1
            return res
        
        
