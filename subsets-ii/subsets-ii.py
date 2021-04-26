class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def backtrack(path, i):
            res.append(path[:]) # goal

            for j in range(i, len(nums)): # choices
                if j > i and nums[j] == nums[j-1]: # constraint
                    continue
                path.append(nums[j]) # choose
                backtrack(path, j+1) # explore
                path.pop()           # unchoose 

        nums.sort()
        backtrack([], 0)
        return res