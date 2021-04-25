class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):
            # 3. goal
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] not in path: # can use set
                    path.append(nums[i])  
                    backtrack(nums, path)
                    path.pop()   
                    
        backtrack(nums, [])
        return res

    