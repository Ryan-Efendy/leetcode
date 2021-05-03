class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
         ]
         
        1. Check edges (optimize just first & last row) for any O's -> convert it to a dummy char '#'
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","#","X","X"]
         ]
         
         2. Convert remaining O's to X's and convert back any #'s to O's
        [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","#","X","X"]
         ]
         
        [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
         ]
        """
        def dfs(i, j):
            board[i][j] = '#'
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    dfs(x, y)
                    
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'