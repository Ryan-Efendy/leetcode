class Solution:
    def reorganizeString(self, S: str) -> str:
        charFreqMap = collections.Counter(S)

        maxHeap = []
        # add all characters to the max heap
        for char, freq in charFreqMap.items():
            heappush(maxHeap, (-freq, char))

        res = []
        while len(maxHeap) > 1:
            currFreq, currChar = heappop(maxHeap)
            nextFreq, nextChar = heappop(maxHeap)
            
            # append the current character to the result string and decrement its count
            res.append(currChar)
            res.append(nextChar)
            
            # add the previous entry back in the heap if its frequency is greater than zero
            if -currFreq > 1:
                heappush(maxHeap, (-(-currFreq - 1), currChar))
            if -nextFreq > 1:
                heappush(maxHeap, (-(-nextFreq - 1), nextChar))
                
        if maxHeap:
            freq, char = heappop(maxHeap)
            if -freq > 1:
                return ''
            res.append(char)

        # if we were successful in appending all the characters to the result string, return it
        # return ''.join(res) if len(res) == len(S) else ""
        return ''.join(res)