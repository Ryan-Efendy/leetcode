class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        unique = collections.Counter(nums)
        def backtrack(nums, path):
            if len(path) == len(nums): # 3. goal reached
                res.append(path[:])
                return
            # handles duplicate
            for num in unique: # 1. Choices
                if unique[num] == 0: # 2. Constraint
                    continue
                unique[num] -= 1
                path.append(num)  # choose
                
                backtrack(nums, path) # explore
                
                path.pop()            # unchoose
                unique[num] += 1
                    
        backtrack(nums, [])
        return res