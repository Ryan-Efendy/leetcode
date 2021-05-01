class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(0, min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                heappush(maxHeap, (-(nums1[i] + nums2[j]), i, j))
                if len(maxHeap) > k:
                    heappop(maxHeap)

        result = []
        while maxHeap:
            num, i, j = heappop(maxHeap)
            result.append([nums1[i], nums2[j]])

        return result