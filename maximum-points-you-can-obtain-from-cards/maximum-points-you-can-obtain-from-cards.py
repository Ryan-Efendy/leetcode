class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        k = 3 | n-k = 5
        XXXXXXXX sliding window 000
        XXXXX000 instead of finding max score, find min score & subtract from total
        0XXXXX00
        00XXXXX0
        000XXXXX
        '''
        n = len(cardPoints)
        pre_sums = [0]
        for cardPoint in cardPoints:
            pre_sums.append(cardPoint+pre_sums[-1])

        min_array_sum = math.inf
        for left in range(k+1):
            # A[i, j] = A[j] - A[i]
            min_array_sum = min(min_array_sum, pre_sums[left+n-k] - pre_sums[left])

        return pre_sums[-1] - min_array_sum