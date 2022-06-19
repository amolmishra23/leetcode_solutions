class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.arr = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
            if len(cur.arr)<3: cur.arr.append(word)
                
    def find(self, word):
        res, cur = [], self.root
        for ch in word:
            cur = cur.children[ch]; res.append(cur.arr)
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie=Trie()
        for prod in sorted(products): trie.insert(prod)
        return trie.find(searchWord)