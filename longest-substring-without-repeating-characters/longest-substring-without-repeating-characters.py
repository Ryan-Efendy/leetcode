class Solution:
    '''
    s = "abcabcbb"
            j
          i
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, i, j = 0, 0, 0
        hash_set = set()
        while j < len(s):
            while s[j] in hash_set:
                hash_set.remove(s[i])
                i += 1   
            hash_set.add(s[j])
            j += 1
            max_len = max(max_len, j-i)
        return max_len
        
        
        
