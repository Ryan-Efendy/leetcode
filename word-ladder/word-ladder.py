class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        https://www.youtube.com/watch?v=ox3VMAYVmn8
        https://www.youtube.com/watch?v=5iFZP-f40iI
        https://leetcode.com/problems/word-ladder/discuss/346920/Python3-Breadth-first-search
        
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5 shortest transformation sequence: hit -> hot -> dot -> dog -> cog
        
                            hot
                           /   \
                        dot --- lot
                         |       |
                        dog --- log     
                          \     /
                            cog 
        
        unweighted undirected graph, shortest path use BFS!
        preprocessing to reduce computation complexity -> wildcard
        { 
            *ot : ["hot", "dot", "lot"]
            h*t : ["hot"]
            ho* : ["hot"]
            d*t : ["dot"]
            do* : ["dot", "dog"]
            *og : ["dog", "log", "cog"]
            d*g : ["dog"]
            l*t : ["lot"]
            lo* : ["lot", "log"]
            l*g : ["log"]
            c*g : ["cog"]
            co* : ["cog"]
        }
        '''        
        def construct_dict(wordList):
            d = collections.defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + "*" + word[i+1:]
                    d[s].append(word)
            return d

        def bfs(begin, end, dict_words):
            queue = deque([(begin, 1)])
            visited = set()
            
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "*" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        d = construct_dict(wordList)
        return bfs(beginWord, endWord, d)