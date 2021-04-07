class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        s = ADOBECODEBANC t = ABC
             i
                    j
        {A: 1, B: 0, C: 0, D: -1, ....}
        counter = 2
        '''
        i = 0
        minLen, res = math.inf, ''
        counter, count = collections.Counter(t), 0

        for j, ch in enumerate(s):
            counter[ch] -= 1
            if counter[ch] >= 0: # ch is in t
                count += 1

            while count == len(t):
                if minLen > j - i + 1:
                    minLen = j - i + 1
                    res = s[i:j+1]
                counter[s[i]] += 1
                if counter[s[i]] > 0: # ch is in t
                    count -= 1
                i += 1

                
        return res