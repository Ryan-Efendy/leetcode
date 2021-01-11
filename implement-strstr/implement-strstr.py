class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        windowSize = len(needle)
        for i in range(len(haystack)-windowSize+1):
            if haystack[i:i+windowSize] == needle:
                return i
        return -1
        
