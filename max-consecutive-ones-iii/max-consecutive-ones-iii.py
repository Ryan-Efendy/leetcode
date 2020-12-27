class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        res = 0
        i, j = 0, 0
        while j < len(A):
            if not A[j]: k -= 1
            j += 1
            while k < 0:
                if not A[i]: k += 1
                i += 1
            res = max(res, j-i)
        return res
