"""
Usually we use trie to solve all the problems of prefix topic.
Here we need to solve for suffix
hence we create the tree in reverse fashion, and make the queries like prefix.

We need to make queries based on prev queries appended string. 
Hence we keep a list of prev characters appended in a list. 
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        temp_node = self.root
        
        for c in word:
            if c not in temp_node.children:
                temp_node.children[c] = TrieNode()
            temp_node = temp_node.children[c]
        temp_node.is_end = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])
            

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        temp_node = self.trie.root
        
        for i in range(len(self.letters)-1, -1, -1):
            char = self.letters[i]
            if temp_node.is_end: 
                return True
            if char not in temp_node.children:
                return False
            temp_node = temp_node.children[char]
        
        return temp_node.is_end
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)