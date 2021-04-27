class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def findMin(nums: List[int]) -> int:
            lo, hi, pivot = 0, len(nums)-1, None
            while lo < hi:
                mid = lo + (hi-lo)//2
                if nums[mid] == nums[hi]:
                    # find the minimum value index vs. just minimum value
                    if (nums[hi] < nums[hi-1]):
                        pivot = hi
                        break
                    hi -= 1
                elif nums[mid] > nums[hi]:
                    lo = mid + 1
                else:    
                    hi = mid
            return pivot if pivot else lo
        
        def search(nums: List[int], target: int, rotation: int) -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi)//2
                midPlusRotation = (mid + rotation) % len(nums)
                if nums[midPlusRotation] < target:
                    lo = mid + 1
                else:
                    hi = mid
            lo = (lo + rotation) % len(nums) # This is the original LEFT index
            return nums[lo] == target
        
        # Normalize: left - rotation = 0
        rotation = findMin(nums)
        return search(nums, target, rotation)