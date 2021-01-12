class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        i, j = 0, 0
        while j < len(s):
            if s[j] == " ":
                self.reverse(s, i, j-1)
                i = j + 1
            j += 1
        self.reverse(s, i, j-1)
                
    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1
