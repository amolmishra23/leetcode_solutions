class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if beginWord in wordSet:
          wordSet.remove(beginWord)
        
        def neighbors(s):
            for i in range(len(s)):
                chars = list(s)
                for c in ascii_lowercase:
                    chars[i] = c
                    newStr = "".join(chars)
                    if newStr in wordSet:
                        yield newStr
        
        ans = 0
        q = deque([beginWord])
        while q:
            ans += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return ans

                for newStr in neighbors(cur):
                    q.append(newStr)
                    wordSet.remove(newStr)
                    
        return 0  # no such transformation sequence.