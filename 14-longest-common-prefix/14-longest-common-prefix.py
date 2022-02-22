class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word):
        root = self.trie
        
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        
        root['$'] = True
        
    def find_longest_prefix(self):
        root = self.trie
        prefix = []
        
        while root:
            if len(root)>1 or root.get('$')==True: break
            char = root.keys()[0]
            root = root[char]
            prefix.append(char)
            
        return "".join(prefix)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        
        if len(strs)==1: return strs[0]
        
        trie = Trie()
        for s in strs:
            trie.insert(s)
        
        return trie.find_longest_prefix()
        