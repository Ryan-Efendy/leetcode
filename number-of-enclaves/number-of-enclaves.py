class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        https://www.youtube.com/watch?v=1HEWeW5swDA
        We flood-fill the land (change 1 to 0) from the boundary of the grid. Then, we count the remaining land.
        '''
        def dfs(i, j):
            grid[i][j] = 0
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                # If grid[i][j] is 1 on the edge, do DFS and clean all connected 1's
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        # Return sum of left 1's
        return sum(sum(row) for row in grid)
