class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str, k: int = 2) -> int:
        '''
        https://www.youtube.com/watch?v=gj1Y-enAlXM
        
        '''
        counter = collections.defaultdict(int)
        left = 0
        res = 0
        for right, ch in enumerate(s):
            counter[ch] += 1

            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            res = max(res, right - left + 1)

        return res