class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        Input: n = 4, k = 2
        Output:
        [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]
        '''
        res = []
        nums = [i for i in range(1, n+1)]

        def backtrack(path, i):
            if len(path) == k:
                res.append(path[:])

            for j in range(i, len(nums)): # choices
                path.append(nums[j]) # choose
                backtrack(path, j+1) # explore
                path.pop()           # unchoose 

        backtrack([], 0)
        return res