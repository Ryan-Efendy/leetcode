class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        """Initialize your data structure here."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        if not word or not len(word): return
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        if not word or not len(word): return False
        curr = self.root
        for ch in word:
            if ch not in curr.children: return False
            curr = curr.children[ch]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        if not prefix or not len(prefix): return False
        curr = self.root
        for ch in prefix:
            if ch not in curr.children: return False
            curr = curr.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)