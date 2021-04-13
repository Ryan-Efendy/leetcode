class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # index
        windowStart = 0

        for windowEnd in range(len(nums)):
            # if windowEnd is bigger than head of q, pop smaller val from q
            while q and nums[q[-1]] < nums[windowEnd]:
                q.pop()
            q.append(windowEnd)

            # out of range, remove windowStart val from window
            if windowStart > q[0]:
                q.popleft()

            # edge case
            if (windowEnd + 1) >= k:
                res.append(nums[q[0]]) # append top of queue
                windowStart += 1
        return res