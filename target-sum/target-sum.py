class Solution:    
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {} # memo: (target, index) => ans
        return self.dfs(nums, S, 0, memo)
    
    def dfs(self, nums, S, i, memo):
        if i == len(nums):
            if S == 0: return 1
            return 0
        if (S, i) in memo:
            return memo[(S, i)]  # avoid repeated computation
        res = self.dfs(nums, S-nums[i], i+1, memo) + self.dfs(nums, S+nums[i], i+1, memo)
        memo[(S, i)] = res
        return res
        
        
        
        