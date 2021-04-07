class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        AABABBA  k=2
          i

              j

        {A: 2, B: 3}
        maxLen = 5
        maxCount = 3

        (R - L + 1) - maxCount        
        '''
        i, res = 0, 0
        counter, max_count = collections.defaultdict(int), 0

        for j, ch in enumerate(s):
            counter[ch] += 1
            max_count = max(max_count, counter[ch])

            while j - i + 1 - max_count > k:
                counter[s[i]] -= 1
                if not counter[s[i]]:
                    del counter[s[i]]
                i += 1

            res = max(res, j - i + 1)
        return res