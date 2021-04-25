class Solution:
    def findMaximizedCapital(self, numberOfProjects: int, initialCapital: int, profits: List[int], capital: List[int]) -> int:
        minCapitalHeap = [] 
        maxProfitHeap = []

        # insert all project capitals to a min-heap
        for i in range(len(profits)):
            heappush(minCapitalHeap, (capital[i], i))

        # let's try to find a total of 'numberOfProjects' best projects
        availableCapital = initialCapital
        for _ in range(numberOfProjects):
            # find all projects that can be selected within the available capital and insert them in a max-heap
            while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
                capital, i  = heappop(minCapitalHeap)
                heappush(maxProfitHeap, (-profits[i], i))

            # terminate if we are not able to find any project that can be completed within the available capital
            if not maxProfitHeap:
                break

            # select the project with the maximum profit
            availableCapital += -heappop(maxProfitHeap)[0]

        return availableCapital