class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashset = set()
        for ch in s:
            if ch in hashset:
                hashset.remove(ch)
            else:
                hashset.add(ch)
        if len(s) % 2 == 0:
            return len(hashset) == 0
        else:
            return len(hashset) == 1
            
