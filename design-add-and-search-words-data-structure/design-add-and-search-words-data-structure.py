class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        # print("insert: ", word)
        root = self.trie
        
        for char in word:
            if char not in root:
                root[char]={}
            root = root[char]
        
        root["$"] = True
        # print(self.trie)

    def search(self, word: str) -> bool:
        # print("term: ", word)
        node = self.trie
        self.res = False
        self.dfs(node, word)            
        return self.res
    
    def dfs(self, node, word):
        # print(node, word)
        # reached at end of the search
        if not word:
            # if it is a ending word
            if "$" in node: 
                self.res=True
            return
        
        if word[0]==".":
            # if its a dot character, we iterate among all the possible characters.
            for x in node:
                if x=="$": continue
                self.dfs(node[x], word[1:])
                if self.res: return
        else:
            if word[0] not in node: return
            self.dfs(node[word[0]], word[1:])
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)