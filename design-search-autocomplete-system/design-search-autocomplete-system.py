class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.hot = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, sentence: str, time: int) -> None:
        curr = self.root
        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True
        curr.hot -= time

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)
            
        self.search_term = ''
        self.last_node = self.trie.root
        self.no_match = False
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.search_term, 1)
            self.search_term = ''
            self.last_node = self.trie.root
            self.no_match = False
        else:
            self.search_term += c

            if not c in self.last_node.children or self.no_match:
                self.no_match = True
                return []
            
            self.last_node = self.last_node.children[c]
            result = []
            self.dfs(self.last_node, self.search_term, result)

            return [sentences[1] for sentences in sorted(result)[:3]]
    
    def dfs(self, node, path, result):
        if node.isEnd:
            result.append((node.hot, path))
        
        for char in node.children:
            self.dfs(node.children[char], path+char, result)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)