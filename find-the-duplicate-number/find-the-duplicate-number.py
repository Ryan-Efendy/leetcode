class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''   
                0 1 2 3 4
        nums = [1,3,4,2,2] ✅ num `1` is not at its correct place, swap to correct idx
                \U0001f446            don't move on the next num until\U0001f446 is in correct idx
                0 1 2 3 4
        nums = [3,1,4,2,2] ✅ num `3` is not at its correct place, swap to correct idx
                \U0001f446
                0 1 2 3 4
        nums = [2,1,4,3,2] ✅ num `2` is not at its correct place, swap to correct idx
                \U0001f446
                0 1 2 3 4
        nums = [4,1,2,3,2] ✅ num `4` is not at its correct place, swap to correct idx
                \U0001f446
                0 1 2 3 4
        nums = [2,1,2,3,4] ❌  while swapping the num w/ its index are already the same -> dup❗
                \U0001f446
        '''
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]  # swap
                else:
                    return nums[i]
            else:
                i += 1
        return nums