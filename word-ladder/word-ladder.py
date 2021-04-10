class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set: return 0
        
        q = deque([(beginWord, 1)])
        
        while q:
            curr, depth = q.popleft()
            if curr == endWord: return depth
            
            for i in range(len(curr)):
                for j in string.ascii_lowercase:
                    temp = curr[:i]+j+curr[i+1:]
                    if temp in word_set:
                        word_set.remove(temp)
                        q.append([temp, depth+1])
        
        return 0