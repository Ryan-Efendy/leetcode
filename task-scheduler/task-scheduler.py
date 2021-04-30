class Solution:
    def leastInterval(self, tasks: List[str], k: int) -> int:
        '''
        1. create freq counter
        2. while maxHeap:
            iterate k + 1 times (Greedy)
                execute task, decrease freq of task and put in waitList
                
                put tasks in waitList back to maxHeap
                
                if iteration we're not able to execute k+1 tasks, CPU has to be idle for the remaining time until next iter
        '''
        intervalCount = 0
        taskFreqMap = collections.Counter(tasks)

        maxHeap = []
        # add all tasks to the max heap
        for char, freq in taskFreqMap.items():
            heappush(maxHeap, (-freq, char))

        while maxHeap:
            waitList = []
            n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
            while n > 0 and maxHeap:
                intervalCount += 1
                freq, char = heappop(maxHeap)
                if -freq > 1:
                    # decrement the freq and add to the waitList
                    waitList.append((freq+1, char))
                n -= 1

            # put all the waiting list back on the heap
            for freq, char in waitList:
                heappush(maxHeap, (freq, char))

            if maxHeap:
                intervalCount += n  # we'll be having 'n' idle intervals for the next iteration

        return intervalCount
