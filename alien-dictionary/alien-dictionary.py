class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Example1
        words:  pair-wise ordering 
        "wrt",               graph    in_degrees
        "wrf",   t->f    =>  t: [f],     t: 1
        "er",    w->e        w: [e],     w: 0 ✅  
        "ett",   r-›t        r: [t],     r: 1
        "rftt",  e->r        e" [r]      e: 1
                  ^    
                  (directed) graph, use topological sort
          w->e->r->t->f  
          
         BFS with adj list and in_degress, 
         decrement in degrees for nodes, when it reach 0
         mean we processes all the nodes before it, so we can put node on to ordering
         
         DFS
        '''
        # init adjcency list & inDegrees
        # get unique chars i.e. words=["wrt","wrf","er","ett","rftt"]
        uniqueChars = {char for word in words for char in word} # {'t', 'f', 'e', 'r', 'w'}
        adjList = collections.defaultdict(list) # {'t': ['f'], 'w': ['e'], 'r': ['t'], 'e': ['r'] 
        inDegrees = collections.defaultdict(int) # {'f': 1, 'e': 1, 't': 1, 'r': 1}
        res = []

        # check word pair, char pair, if the same continue else there's ordering diff -> build graph
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    continue
                # build graph if there's a difference between c1 & c2
                inDegrees[c2] += 1
                adjList[c1].append(c2)
                break # after the first inequaility we can break, don't need to compare the rest of word pair

            # for-else statement: only enter here if you didn't 'break' inside the for loop above
            else:
                if len(w1) > len(w2): return ''
        # BFS
        # find node w/ no indegree
        queue = deque(ch for ch in uniqueChars if inDegrees[ch] == 0)
        while queue:
            node = queue.popleft()
            res.append(node) # add to ordering
            for nxt_node in adjList[node]:
                inDegrees[nxt_node] -= 1 # decrement indegree after processing the prevNode 
                # if edge has no indegree can enqueue
                if not inDegrees[nxt_node]: queue.append(nxt_node)
        # check cycle: res <= total # nodes
        return ''.join(res) if len(res) == len(uniqueChars) else ''