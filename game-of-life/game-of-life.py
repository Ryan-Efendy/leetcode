class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        m, n = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        
        for i in range(m):
            for j in range(n):
                # if board[i][j] == 1:
                live_nei = 0
                for dx, dy in directions:
                    ii = i + dx
                    jj = j + dy
                    if 0 <= ii < m and 0 <= jj < n and abs(board[ii][jj]) == 1:
                        live_nei += 1
                
                # live -> dead
                if board[i][j] == 1 and (live_nei < 2 or live_nei > 3):
                    board[i][j] = -1
                # dead -> live
                if board[i][j] == 0 and live_nei == 3:
                    board[i][j] = 2
                    
        # clean up
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1