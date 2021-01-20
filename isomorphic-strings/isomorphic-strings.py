class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2, mapping = collections.defaultdict(int), collections.defaultdict(int), {}
        for ch1, ch2 in zip(s, t):
            d1[ch1] += 1
            d2[ch2] += 1
            if ch1 in mapping:
                if mapping[ch1] != ch2: return False
            else:
                mapping[ch1] = ch2
        for k, v in mapping.items():
            if d1[k] != d2[v]: return False
        return True
