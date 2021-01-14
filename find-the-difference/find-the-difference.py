class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ord(t[-1])
        for x, y in zip(s, t):
            res ^= ord(x) ^ ord(y)
        return chr(res)
