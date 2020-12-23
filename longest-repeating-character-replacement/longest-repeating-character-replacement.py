class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = collections.defaultdict(int)
        i, j, maxCount,maxLen = 0, 0, 0, 0
        while j < len(s):
            d[s[j]] += 1
            maxCount = max(maxCount, d[s[j]])
            j += 1
            while j - i - maxCount > k:
                d[s[i]] -= 1
                i += 1
            maxLen = max(maxLen, j - i)
        return maxLen
