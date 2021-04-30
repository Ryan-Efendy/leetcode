class Solution:
    def reorganizeString(self, s: str, k: int = 2) -> str:
        '''
        same as Rearrange String k Distance Apart, where k = 2
        '''
        # edge case
        if k == 0: # k <= 1
            return s

        charFreqMap = collections.Counter(s)
        maxHeap = []
        for char, freq in charFreqMap.items():
            heappush(maxHeap, (-freq, char))

        queue = deque()
        res = []
        while maxHeap:
            freq, char = heappop(maxHeap)
            # append the current character to the result string and decrement its count
            res.append(char)
            # decrement the freq and append to the queue
            queue.append((char, freq+1)) # same as -(-freq - 1)
            if len(queue) == k:
                char, freq = queue.popleft()
                if -freq > 0:
                    heappush(maxHeap, (freq, char))

        # if we were successful in appending all the characters to the result string, return it
        return ''.join(res) if len(res) == len(s) else ""