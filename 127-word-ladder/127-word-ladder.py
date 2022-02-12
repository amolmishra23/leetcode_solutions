class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set: return 0
        
        q = deque([(beginWord, 1)])
        chars = {x for word in wordList for x in word}       
        
        while q:
            word, level = q.popleft()
            if word == endWord: return level
            
            for i in range(len(word)):
                for c in chars:
                    temp = word[:i]+c+word[i+1:]
                    if temp in word_set:
                        q.append((temp, level+1))
                        word_set.remove(temp)
                        
        return 0