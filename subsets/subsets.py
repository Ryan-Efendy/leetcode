class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [1,2,3]
                        [ ] ✅
                      /  |  \  
                    1    2    3
                  [1]✅  [2]✅  [3]✅
                 /  \      \   
                2    3       3
            [1,2]✅ [1,3]✅  [2,3]✅
               |
               3
            [1,2,3]✅ 
        
        Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        
        '''
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res