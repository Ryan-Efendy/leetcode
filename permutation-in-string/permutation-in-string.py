class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        minLen = math.inf
        counter, count = collections.Counter(s1), 0

        for j, ch in enumerate(s2):
            counter[ch] -= 1
            if counter[ch] >= 0: # ch is in t
                count += 1

            while count == len(s1):
                minLen = min(minLen, j - i + 1)
                counter[s2[i]] += 1
                if counter[s2[i]] > 0: # ch is in t
                    count -= 1
                i += 1
        
        return minLen == len(s1)