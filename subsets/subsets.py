class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, 0, [], res)
        return res
        
    def backtrack(self, nums, i, path, res):
        if i >= len(nums):
            res.append(path[:])
            return
        path.append(nums[i])
        self.backtrack(nums, i+1, path, res)
        path.pop()
        self.backtrack(nums, i+1, path, res)