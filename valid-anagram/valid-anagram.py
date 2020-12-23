class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = collections.Counter(s)
        for ch in t:
            counter[ch] -= 1
        
        for ch in s:
            if counter[ch]: return False
        
        return True
