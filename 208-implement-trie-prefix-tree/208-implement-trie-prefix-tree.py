class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        root = self.trie
        
        for x in word:
            if x not in root: root[x] = {}
            root = root[x]
            
        root["$"] = {}

    def search(self, word: str) -> bool:
        root = self.trie
        
        for c in word:
            if c not in root: return False
            root = root[c]
            
        return "$" in root

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        
        for x in prefix:
            if x not in root: return False
            root = root[x]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)