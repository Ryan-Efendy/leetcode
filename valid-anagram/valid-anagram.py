class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freq = [0]*26
        for ch1, ch2 in zip(s, t):
            freq[ord(ch1) - ord('a')] += 1
            freq[ord(ch2) - ord('a')] -= 1
        return not any(freq)
