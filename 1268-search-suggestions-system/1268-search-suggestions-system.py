class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.arr=[]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for letter in word:
            cur = cur.children[letter]
            if len(cur.arr)<3: cur.arr.append(word)

    def find(self,word):
        res=[]
        cur=self.root
        for el in word:
            cur=cur.children[el]
            res.append(cur.arr)
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie=Trie()
        for el in sorted(products):
            trie.insert(el)
        return trie.find(searchWord)