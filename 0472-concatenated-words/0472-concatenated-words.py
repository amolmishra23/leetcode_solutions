class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x: len(x))
        words_set = set()
        
        def can_build(w):
            if w in words_set: return True    
            for i in range(1, len(w)):
                if w[:i] in words_set and can_build(w[i:]): return True
            return False
        
        res = []
        for w in words:
            if can_build(w): res.append(w)
            words_set.add(w)
            
        return res