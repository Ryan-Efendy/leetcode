class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        if len(words) == 0: return ""
        if len(words) == 1: return words[0]
        lcp = words[0]
        for word in words[1:]:
            i = 0
            while i < len(word) and i < len(lcp) and word[:i] == lcp[:i]:
                i += 1
            lcp = lcp[:i] if lcp[:i] == word[:i] else lcp[:i-1]
        return lcp
                    
