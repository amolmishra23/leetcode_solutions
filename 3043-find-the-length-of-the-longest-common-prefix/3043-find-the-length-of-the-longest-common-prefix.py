class TrieNode:
    def __init__(self):
        self.val = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, a):
        curr = self.root
        tmp = str(a)
        
        for ch in tmp:
            if ch not in curr.val:
                curr.val[ch] = TrieNode()
            curr = curr.val[ch]
            
        curr.is_end = True
        
    def prefix_match(self, b):
        curr = self.root
        tmp = str(b)
        res = 0
        
        for ch in tmp:
            if ch not in curr.val:
                break
            curr = curr.val[ch]
            res += 1
            
        return res
        
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t = Trie()
        
        for val in arr1:
            t.insert(val)
            
        res = 0
        for val in arr2:
            res = max(res, t.prefix_match(val))
            
        return res

class Solution1:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
            
        prefix_set = set()
        
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n//10
                
        res = 0
        for n in arr2:
            while n and n not in prefix_set:
                n = n//10
                
            if n:
                res = max(res, len(str(n)))
                
                
        return res