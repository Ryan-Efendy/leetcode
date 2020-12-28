class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def getKMostCount(k):
            d = collections.defaultdict(int)
            i, j = 0, 0
            max_len = 0
            while j < len(A):
                d[A[j]] += 1
                j += 1
                while len(d) > k:
                    d[A[i]] -= 1
                    if not d[A[i]]: d.pop(A[i], None)
                    i += 1
                max_len += j-i
            return max_len
        return getKMostCount(K) - getKMostCount(K-1)
