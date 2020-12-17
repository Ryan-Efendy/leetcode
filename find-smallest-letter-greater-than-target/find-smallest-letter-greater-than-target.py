class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        while l < r:
            m = l + (r-l)//2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
​
        if letters[l] <= target:
            return letters[(l+1)%len(letters)]
        else:
            return letters[l]
