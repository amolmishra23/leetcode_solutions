class Trie:
    def __init__(self):
        self.trie = {}
        
    def add(self, word):
        root = self.trie
        
        for ch in word:
            root.setdefault(ch, {})
            root = root[ch]
        
        root["$"] = True
        
    def exists(self, word):
        root = self.trie
        self.res = ""
        self.dfs(word, root, 0)
        return self.res
    
    def dfs(self, word, root, i):
        if "$" in root:
            self.res = word[:i]
            return
        
        if i>=len(word): return
            
        if word[i] not in root: return
        self.dfs(word, root[word[i]], i+1)
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary: trie.add(word)
            
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            prefix = trie.exists(sentence[i])
            if prefix!="": sentence[i]=prefix
                
        return " ".join(sentence)