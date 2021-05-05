class Solution:
    def uniquePaths(self, m: int, n: int, memo: dict = {}) -> int:
        '''
        base case m == 1 and n ==1 => 1
        base case m == 0 or == 0 => 0
        uniquePaths(2, 3) => 3
        '''
        if (m, n) in memo: return memo[(m, n)]
        if (n, m) in memo: return memo[(n, m)]
        if m == 0 or n == 0: return 0
        if m == 1 and n == 1: return 1
        # down, right
        ans = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        memo[(m, n)] = ans
        memo[(n, m)] = ans
        return ans