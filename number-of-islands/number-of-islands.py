class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:        
        if not grid or not len(grid) or not len(grid[0]): return 0
        visited = set()
        res = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            visited.add((i,j)) # grid[i][j] = '#'
            # check up, right, down, left
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x,y) not in visited and grid[x][y] == '1':
                    dfs(x, y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
        return res