class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, 10)]
        
        def backtrack(path, start, k, target):
            if k == 0 and target == 0: # goal
                res.append(path[:])
                return
            for i in range(start, len(nums)): # choices
                path.append(nums[i]) # choose
                backtrack(path, i+1, k-1, target-nums[i]) # explore
                path.pop()           # unchoose 
    
        backtrack([], 0, k, target)
        return res