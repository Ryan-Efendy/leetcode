class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(lambda: [])
        for str in strs:
            sorted_str = ''.join(sorted(str))
            d[sorted_str] += [str]
        return d.values()
