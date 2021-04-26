class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set() 
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if 0 <= r < m and 0 <= c < n and word[i] == board[r][c] and (r,c) not in visited:
                visited.add((r, c))
                for dx, dy in directions:
                    if dfs(r + dx, c + dy, i + 1):
                        return True
                visited.remove((r, c))
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0): return True
        return False                    