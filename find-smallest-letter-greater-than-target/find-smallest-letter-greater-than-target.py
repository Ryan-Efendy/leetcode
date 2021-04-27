class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def bisect_left(letters: List[str], target: str) -> int:
            l, r = 0, len(letters)
            while l < r:
                m = l + (r-l)//2
                if letters[m] <= target:
                    l = m + 1
                else:
                    r = m
            return letters[l % len(letters)]
        
        return bisect_left(letters, target)
        
        