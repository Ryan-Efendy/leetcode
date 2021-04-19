class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m: return []

        p_count = Counter(p)
        s_count = Counter()

        result = []
        for i in range(n):
            windowStart, windowEnd = i-m, i
            s_count[s[windowEnd]] += 1
            if i >= m:
                if s_count[s[windowStart]]==1:
                    del s_count[s[windowStart]]
                else:
                    s_count[s[windowStart]] -= 1
            if p_count == s_count:
                result.append(windowStart + 1)
        return result