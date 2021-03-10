class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k == 0: return res
        self.backtrack(1, n, k, [], res)
        return res
        
    def backtrack(self, start, n, k, path, res):
        if len(path) == k:
            res.append(path[:])
        
        for i in range(start, n+1):
            if len(path) < k:
                path.append(i)
                self.backtrack(i+1, n, k, path, res)
                path.pop()
                
        
        