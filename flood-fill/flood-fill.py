class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        srcColor = image[sr][sc]
        if srcColor == newColor: return image
        image[sr][sc] = newColor
        self.dfs(image, sr, sc, srcColor, newColor)
        return image
        
    def dfs(self, image: List[List[int]], sr: int, sc: int, srcColor:int, newColor: int):
        for r, c in [(1,0), (-1,0), (0,1), (0,-1)]:
            i, j = sr + r, sc + c
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == srcColor:
                image[i][j] = newColor
                self.dfs(image, i, j, srcColor, newColor)