class Solution:
    def groupStrings(self, words: List[str]) -> List[List[str]]:
        def get_hash(s):
            return tuple((ord(c) - ord(s[0])) % 26 for c in s)
        
        d = collections.defaultdict(list)
        for word in words:
            d[get_hash(word)] += [word]
        return d.values()
