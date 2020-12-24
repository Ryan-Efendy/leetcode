class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = collections.Counter(p)
        i, j = 0, 0
        count, res = len(counter), []
        while j < len(s):
            if s[j] in counter:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    count -= 1
            j += 1
            if count == 0:
                res.append(i)
            if j - i > len(p)-1:
                if s[i] in counter:
                    if counter[s[i]] == 0:
                        count += 1
                    counter[s[i]] += 1
                i += 1
        return res
