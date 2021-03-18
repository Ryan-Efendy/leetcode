import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        candidates = count.keys()
        res = sorted(candidates, key=lambda x: (-count[x], x))
        return res[:k]