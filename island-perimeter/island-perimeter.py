class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        DFS on every (unvisited) land, go 4 directions (up, down, left, right) if out of bound or is water return 1 else 0
        '''
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0

            visited.add((i, j))
            return dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)