class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = dict()
        i, j = 0, 0
        max_len = 0
        while j < len(s):
            d[s[j]] = d.get(s[j], 0) + 1
            j += 1
            while len(d) > 2:
                d[s[i]] -= 1
                if not d[s[i]]: d.pop(s[i], None)
                i += 1
            max_len = max(max_len, j-i)
        return max_len
