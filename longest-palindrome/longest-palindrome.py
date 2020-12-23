class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        for ch in s:
            if ch in hashset:
                hashset.remove(ch)
            else:
                hashset.add(ch)
        if len(hashset) == 0: return len(s)
        return len(s) - len(hashset) + 1
