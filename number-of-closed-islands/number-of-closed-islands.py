class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        same as number of islands except only count CLOSED island.
        check if island is on the edge -> if i == 0 or i == m -1 or j == 0 or j == n - 1
        use a flag 'isClosed' set it False if it's on the edge
        
        https://www.youtube.com/watch?v=MnD8KhBHgRo
        https://www.youtube.com/watch?v=uwzCdK9M1PY
        
        
        or similar to Number of Enclaves.
        (1) remove all land connected to the edges using flood fill.
        (2) count and flood-fill the remaining islands.
        
        [
            [1, 1, 1, 1, 1, 1, 1, 0], 
            [1, 0, 0, 0, 0, 1, 1, 0], 
            [1, 0, 1, 0, 1, 1, 1, 0], 
            [1, 0, 0, 0, 0, 1, 0, 1], 
            [1, 1, 1, 1, 1, 1, 1, 0]
         ]

        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

        '''
        def dfs(i, j):
            grid[i][j] = 1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    dfs(x, y)

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                # If grid[i][j] is 0 on the edge, do DFS convert it to a 1
                if grid[i][j] == 0 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
                        
        print(grid)
        return self.numIslands(grid)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:        
        visited = set()
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(grid, i, j):
            visited.add((i,j)) # grid[i][j] = '#'
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x,y) not in visited and grid[x][y] == 0:
                    dfs(grid, x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    res += 1
                    dfs(grid, i, j)
        return res