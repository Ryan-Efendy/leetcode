class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = collections.defaultdict(int)
        char_count = len(t)
        min_window_start, min_window_length = 0, math.inf
        for ch in t:
            d[ch] += 1
        i, j = 0, 0
        while j < len(s):
            if d[s[j]] > 0: char_count -= 1
            d[s[j]] -= 1
            j += 1
            
            while char_count == 0:
                if min_window_length > j-i:
                    min_window_length = j-i
                    min_window_start = i
                d[s[i]] += 1
                if d[s[i]] > 0: char_count += 1
                i += 1
        return "" if min_window_length == math.inf else s[min_window_start:min_window_start+min_window_length]
            
            
​
