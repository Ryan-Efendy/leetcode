class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True
            
    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, word: str) -> bool:
            for i, ch in enumerate(word):
                if ch == '.':
                    for child in node.children.values():
                        if dfs(child, word[i+1:]): return True
                    return False
                if ch in node.children:
                    node = node.children[ch]
                else:
                    return False
            return node.isEnd 
        
        curr = self.root
        return dfs(curr, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)