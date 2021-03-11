class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(candidates, target, 0, [], res)
        return res
        
    def backtrack(self, candidates, target, i, tmp, res):
        if target == 0:
            res.append(tmp[:])
            return
        elif target < 0:
            return
        
        for j in range(i, len(candidates)):
            tmp.append(candidates[j])
            self.backtrack(candidates, target-candidates[j], j, tmp, res)
            tmp.pop()