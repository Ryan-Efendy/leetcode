class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights2 = sorted(heights)
        res = 0
        for height, height2 in zip(heights, heights2):
            if height != height2: res += 1
        return res
