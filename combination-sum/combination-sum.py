class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Input: candidates = [2,7,3,6], target = 7
        1. sort candidates = [2,3,6,7]
        Output: [[2,2,3],[7]]
        
        '''
        res = []
        def backtrack(path, start, end, target):
            if target == 0: # goal
                res.append(path[:])
            elif target > 0: #
                for i in range(start, end): # choices
                    path.append(candidates[i]) # choose
                    backtrack(path, i, end, target-candidates[i]) # explore
                    path.pop()           # unchoose 

        backtrack([], 0, len(candidates), target)
        return res        