class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        divide and conquer O(N^2) time O(N) space
        longestSubstr(i, j) = max(longestSubstr(i, mid), longestSubstr(mid+1, j))
        finding mid (split position) - invalid char or char's freq < k
        
        s = ababcbaaed k = 2
        {a: 4, b: 3, c: 1, d: }
        '''
        def partition(left, right):
            counter = defaultdict(int)
            
            for i in range(left, right+1):
                counter[s[i]] += 1

            for mid in range(left, right+1):
                if counter[s[mid]] < k:
                    return max(partition(left, mid-1), partition(mid+1, right))

            return right - left + 1

        return partition(0, len(s)-1)
    
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        Sliding Window O(N) time O(1) space
        
        s = "abababbdabcabc" k = 2
        maxUniqe = 4 => a,b,c,d
        
        currUnique = 1 
        aba[bb]dabcabc       MAX(-1, 2) = 2

        currUnique = 2
        [abababb]dabcabc     MAX(2,7) = 7
        
        currUnique = 3  
        abababbd[abcabc]     MAX(7,6) = 7
        
        currUnique = 4
        invalid b/c freq(d) < k
        '''
        freq = Counter(s)
        maxUnique = len(freq)
        ans = 0

        # need to consider all scenarios/subarrs/unique chars
        for currUnique in range(1, maxUnique+1):
            counter = defaultdict(int)
            left = 0
            for right in range(len(s)):
                counter[s[right]] += 1

                # maintain the sliding window while len(counter) : currUnique:
                while len(counter) > currUnique:
                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        del counter[s[left]]
                    left += 1

                # now with a valid sliding window, we check the frequency
                if all(count >= k for key, count in counter.items()):
                    ans = max(ans, right - left + 1)

        return ans