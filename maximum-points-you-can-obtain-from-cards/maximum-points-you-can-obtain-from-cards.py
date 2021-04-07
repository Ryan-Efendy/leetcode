class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        O(N) Time, O(1) Space
        running sum instead of presum
        k = 3 | n-k = 5
        01234567
        XXXXXXXX sliding window 000
        XXXXX000 instead of finding max score, find min score & subtract from total
        0XXXXX00
        00XXXXX0
        000XXXXX
        '''
        n = len(cardPoints)
        running_sum = 0
        left = right = 0
        min_sum = math.inf

        for right, num in enumerate(cardPoints):
            running_sum += num

            if right - left > n-k-1:
                running_sum -= cardPoints[left]
                left += 1

            if right - left == n-k-1:
                min_sum = min(min_sum, running_sum)

        return sum(cardPoints) - min_sum

#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         '''
#         O(N) Time & Space
#         k = 3 | n-k = 5
#         XXXXXXXX sliding window 000
#         XXXXX000 instead of finding max score, find min score & subtract from total
#         0XXXXX00
#         00XXXXX0
#         000XXXXX
#         '''
#         n = len(cardPoints)
#         pre_sums = [0]
#         for cardPoint in cardPoints:
#             pre_sums.append(cardPoint+pre_sums[-1])

#         min_array_sum = math.inf
#         for i in range(k+1):
#             # A[i, j] = A[j] - A[i]
#             min_array_sum = min(min_array_sum, pre_sums[i+n-k] - pre_sums[i])

#         return pre_sums[-1] - min_array_sum