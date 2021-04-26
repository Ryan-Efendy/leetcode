class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # visited = set() 
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c, i):
            if i == len(word): # 3. goal reached
                return True
            # 2. Constraint 
            if 0 <= r < m and 0 <= c < n and word[i] == board[r][c]:
                # visited.add((r, c)) # a. choose
                ch = board[r][c]
                board[r][c] = '#'
                for dx, dy in directions: # 1. Choices
                    if dfs(r + dx, c + dy, i + 1): # b. explore
                        return True 
                # visited.remove((r, c)) # c. unchoose
                board[r][c] = ch
            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0): return True
        return False                    