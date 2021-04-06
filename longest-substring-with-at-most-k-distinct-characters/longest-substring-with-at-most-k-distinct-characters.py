class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i, j, res = 0, 0, 0
        counter = collections.defaultdict(int)
        while j < len(s):
            counter[s[j]] += 1
            while len(counter) > k:
                counter[s[i]] -= 1
                if not counter[s[i]]:
                    del counter[s[i]]
                i += 1
            
            res = max(res, j - i + 1)
            j += 1
            
        return res