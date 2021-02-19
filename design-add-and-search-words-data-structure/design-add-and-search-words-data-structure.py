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
        curr = self.root
        stack = [(curr, word)]
        while stack:
            node, word = stack.pop()
            if not word:
                if node.isEnd:
                    return True
            elif word[0] in node.children:
                stack.append((node.children[word[0]], word[1:]))
            elif word[0] == '.':
                for child in node.children.values():
                    stack.append((child, word[1:]))
                
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)