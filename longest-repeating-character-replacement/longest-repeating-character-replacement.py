class Solution:
    '''
    s = "AABABBBBBBBA", k = 1
         l
             r
    {
        A: 3
        B: 1
    }
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, max_len, max_count = 0, 0, 0, 0
        d = collections.defaultdict(int)
        while j < len(s):
            d[s[j]] += 1
            max_count = max(max_count, d[s[j]])
            j += 1
            while j-i-max_count > k:
                d[s[i]] -= 1
                i += 1
            max_len = max(max_len, j - i)
        return max_len
