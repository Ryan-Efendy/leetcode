class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        def binary_search(nums, target):
            l, r = 0, len(nums)-1
            while l < r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1
    
        
        nums.sort()
        for i, num in enumerate(nums):
            j = binary_search(nums, num*2)
            if j != -1 and i != j and nums[j] == num*2: return True
        return False
