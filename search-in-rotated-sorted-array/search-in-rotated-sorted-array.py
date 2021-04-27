class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        |       /            |  /
        |     /        =>    |/
        |   /                |      /      
        | /                  |    /
        /_________           |__/________
        
        1. check which half is sorted 
               \U0001f447          \U0001f447
        nums = [4,5,6,7,0,1,2] target = 0
                      \U0001f446     
        2. check if the target is in the range of the sorted half.
            is 0 between 4 <= x <= 7 ✅ or 0 <= x <= 2
            

        is 0 between 4 <= x <= 7 or between 0 <= x <= 4 ✅
        search in the right halve
               \U0001f447          \U0001f447
        nums = [6,7,8,1,2,4,5]
                      \U0001f446
        '''
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            # left sorted portion
            elif nums[mid] >= nums[lo]:
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # right sorted portion
            else:
                if target <= nums[hi] and target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1