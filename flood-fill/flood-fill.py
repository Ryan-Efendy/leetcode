class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        DFS: Find a connected component (CC) of (sc, sr)
        Replace the color of all node in that CC
        
        [               sr = 1, sc = 1, newColor = 2
            [1,1,1],
            [1,1,0],    image[sr][sc] = 1
            [1,0,1]     go up, down, left & right if CC color is the same as image[sr][sc] fill it
        ]
        
        [
            [2,2,2],
            [2,2,0],
            [2,0,1]
        ]
        '''
        res = 0
        m, n = len(image), len(image[0])
        srcColor = image[sr][sc]

        def dfs(i, j):
            image[i][j] = newColor
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and image[x][y] == srcColor:
                    dfs(x, y)

        if image[sr][sc] == newColor:
            return image
        
        dfs(sr, sc)
        return image