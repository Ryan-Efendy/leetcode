class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        sets = set()
        for char in s:
            if char not in sets:
                sets.add(char)
            else:
                sets.remove(char)
        
        return len(sets) <= 1