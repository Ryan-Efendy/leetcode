class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:        
        if not grid or not len(grid) or not len(grid[0]): return 0
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = collections.deque()
        visited = set()
        islands = 0
        m, n = len(grid), len(grid[0])
        
        def bfs(grid, i, j):
            while queue:
                i, j = queue.popleft()
                for direction in directions:
                    x, y = i + direction[0], j + direction[1]
                    if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited and grid[x][y] == '1':
                        queue.append((x, y))
                        visited.add((x, y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    queue.append((i, j))
                    bfs(grid, i, j)
                    islands += 1
        return islands