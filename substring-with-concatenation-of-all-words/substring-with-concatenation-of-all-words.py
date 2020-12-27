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
        wordBag = Counter(words)   # count the freq of each word
        wordLen, numWords = len(words[0]), len(words)
        res = []
        i = 0
        while i <= len(s) - wordLen * numWords:
            seen = defaultdict(int)   # reset for each i
            for j in range(i, i+wordLen*numWords, wordLen):
                currWord = s[j:j+wordLen]
                if currWord in wordBag:
                    seen[currWord] += 1
                    if seen[currWord] > wordBag[currWord]: break
                else:
                    break
            if seen == wordBag:
                res.append(i)
            i += 1
        return res
        
