class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or not s: return 0
        counter = collections.defaultdict(int)
        left = 0
        res = 0
        for right, ch in enumerate(s):
            # counter[ch] += 1
            while ch in counter:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            counter[ch] += 1
            res = max(res, right - left + 1)
        return res