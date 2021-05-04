class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:   
        visited = set()
        area, maxArea = 0, 0
        m, n = len(grid), len(grid[0])
        

        def dfs(grid, i, j):
            nonlocal area, maxArea
            visited.add((i,j)) # grid[i][j] = '#'
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x,y) not in visited and grid[x][y] == 1:
                    area += 1
                    maxArea = max(area, maxArea)
                    dfs(grid, x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = 1
                    dfs(grid, i, j)
        return max(area, maxArea)