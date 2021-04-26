class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(path, start, target):
            if target == 0: # goal
                res.append(path[:])
            for i in range(start, len(candidates)): # choices
                if candidates[i] > target: # constraint
                    continue
                if i > start and candidates[i] == candidates[i-1]: # constraint
                    continue
                path.append(candidates[i]) # choose
                backtrack(path, i+1, target-candidates[i]) # explore
                path.pop()           # unchoose 
    
        candidates.sort()
        backtrack([], 0, target)
        return res