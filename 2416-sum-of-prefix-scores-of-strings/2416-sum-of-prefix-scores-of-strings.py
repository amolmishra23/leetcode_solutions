class TrieNode:
    def __init__(self):
        self.val = {}
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, w):
        curr = self.root
        
        for ch in w:
            if ch not in curr.val:
                curr.val[ch] = TrieNode()
            curr = curr.val[ch]
            curr.count += 1
            
            
    def score(self, w):
        curr, res = self.root, 0
        
        for ch in w:
            curr = curr.val[ch]
            res += curr.count
            
        return res
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        [t.insert(w) for w in words]
        return [t.score(w) for w in words]