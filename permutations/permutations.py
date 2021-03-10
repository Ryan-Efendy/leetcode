class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, [], res)
        return res
        
    def backtrack(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])    
                self.backtrack(nums, path, res)
                path.pop()
                