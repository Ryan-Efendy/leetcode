class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visitted = set()
        self.backtrack(nums, [], visitted, res)
        return res
        
    def backtrack(self, nums, path, visitted, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if i not in visitted:
                visitted.add(i)    
                self.backtrack(nums, path + [nums[i]], visitted, res)
                visitted.remove(i)
                