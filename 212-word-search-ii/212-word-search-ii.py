class Solution:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word):
        root = self.trie
        
        for x in word:
            if x not in root: root[x] = {}
            root = root[x]
            
        root["$"] = True 
        
    def solve(self, i, j, curr_word, trie):       
        if not 0<=i<self.m or \
        not 0<=j<self.n or \
        not trie or \
        self.board[i][j] not in trie or \
        self.visited[i][j]: return
        
        curr_word.append(self.board[i][j])
        self.visited[i][j] = True
        
        trie = trie[self.board[i][j]]
        if "$" in trie: self.res.add("".join(curr_word))
        
        self.solve(i-1, j, curr_word, trie)
        self.solve(i+1, j, curr_word, trie)
        self.solve(i, j+1, curr_word, trie)
        self.solve(i, j-1, curr_word, trie)
        
        self.visited[i][j] = False
        curr_word.pop()
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        
        self.board = board
        self.m, self.n = len(self.board), len(self.board[0])
        
        self.visited = [[False]*self.n for _ in range(self.m)]

        self.res = set()
        
        for word in words: self.insert(word)
        
        for i in range(self.m):
            for j in range(self.n):
                self.solve(i,j,[], self.trie)
        
        return self.res
        