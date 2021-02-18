class MapSum:
    def __init__(self):
        """Initialize your data structure here."""
        self.trie = Trie()
        self.map = collections.defaultdict(int)
 
    def insert(self, key: str, val: int) -> None:
        if not key or not len(key): return
        if key in self.map:
            self.trie.updateSum(key, self.map[key], val)
        else:
            self.trie.insert(key, val)
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        if not prefix or not len(prefix): return 0
        return self.trie.startsWith(prefix)
        
class TrieNode:
    def __init__(self, val=0):
        self.val = val
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        """Initialize your data structure here."""
        self.root = TrieNode()

    def insert(self, word: str, val: int) -> None:
        """Inserts a word into the trie."""
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(val)
            else:
                curr.children[ch].val += val
            curr = curr.children[ch]
        curr.isEnd = True
        
    def updateSum(self, word: str, prev: int, val: int) -> int:
        curr = self.root
        for ch in word:
            curr.children[ch].val -= prev
            curr.children[ch].val += val
            curr = curr.children[ch]
        
    def startsWith(self, prefix: str) -> int:
        """Returns if there is any word in the trie that starts with the given prefix."""
        curr = self.root
        for ch in prefix:
            if ch not in curr.children: return 0
            curr = curr.children[ch]
        return curr.val
    
    
    

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)