class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            root.insert(word)
        
        words = sentence.split()
        for i, word in enumerate(words):
            replace = root.startsWith(word)
            if replace:
                words[i] = replace
        
        return " ".join(words)
            
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            curr = curr.children[ch]
        curr.isEnd = word
        print(curr.isEnd)

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children: return False
            curr = curr.children[ch]
        return True if curr.isEnd else False

    def startsWith(self, prefix: str) -> str:
        curr = self.root
        for ch in prefix:
            if curr.isEnd: return curr.isEnd
            if ch not in curr.children: return ''
            curr = curr.children[ch]
        return curr.isEnd

        