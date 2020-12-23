class Solution:
    '''
    01234567
    eidboaoo
    
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        i, j = 0, 0
        count, res = len(counter), 0
        while j < len(s2):
            if s2[j] in counter:
                counter[s2[j]] -= 1
                if counter[s2[j]] == 0:
                    count -= 1
            j += 1
            if count == 0: return True
            if j - i > len(s1)-1:
                if s2[i] in counter:
                    if counter[s2[i]] == 0:
                        count += 1
                    counter[s2[i]] += 1
                i += 1
        return False
