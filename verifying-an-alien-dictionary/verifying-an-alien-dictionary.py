class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        https://www.youtube.com/watch?v=jK5a8T9q4pc
        https://www.youtube.com/watch?v=8gCFuDKkmfk
        
        create a mapping for O(1) lookup
        char: weight/idx
        {'h': 0, 'l': 1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'i': 9, 'j': 10, 'k': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

        '''
        order = {letter: idx for idx, letter in enumerate(order)}
        print(order)
        def lex_order(w1, w2):
            for c1, c2 in zip(w1, w2):
                if order[c1] < order[c2]: return True
                if order[c1] > order[c2]: return False
            # w1.startswith(w2), w1 has more 'weight'
            # if equal then is still sorted
            return len(w1) <= len(w2)
        
        for w1, w2 in zip(words, words[1:]):
            if not lex_order(w1, w2): return False
        return True