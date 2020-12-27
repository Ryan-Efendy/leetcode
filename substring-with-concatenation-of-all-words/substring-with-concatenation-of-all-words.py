class Solution:
    '''
    012345678901234567
    barfoothefoobarman
    ---
​
    012345678901234567890123
    barfoofoobarthefoobarman
    '''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counter = Counter(words)   # count the freq of each word
        n, m = len(words[0]), len(words)
        res = []
        i = 0
        while i <= len(s) - n * m:
            seen = defaultdict(int)   # reset for each i
            j = 0
            while j < m:
                currWord = s[i+j*n:i+(j+1)*n]
                if currWord not in counter:
                    break
                seen[currWord] += 1
                if seen[currWord] > counter[currWord]: break
                j += 1
            if j == m:
                res.append(i)
            i += 1
        return res
        
