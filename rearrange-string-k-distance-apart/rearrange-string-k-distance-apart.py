class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        '''
        Input: s = "aabbcc", k = 3
        Counter({'a': 2, 'b': 2, 'c': 2}), k = 3
        
        Counter({'a': 1, 'b': 1, 'c': 1}), k = 3
        res = 'abc'
        
        Counter({}), k = 3
        res = 'abcabc'
        
        Output: "abcabc"
        Explanation: The same letters are at least a distance of 3 from each other.
        
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
