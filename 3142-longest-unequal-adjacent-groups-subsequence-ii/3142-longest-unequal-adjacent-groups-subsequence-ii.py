class Solution:
    def differByOneChar(self, word1, word2):
        if len(word1)!=len(word2): return False
        return sum(c1!=c2 for c1,c2 in zip(word1,word2))<=1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp, parent = [1]*n, [-1]*n
        res = 0

        for i in range(n):
            for j in range(i):
                if groups[i]!=groups[j] and \
                    self.differByOneChar(words[i], words[j]) and \
                    dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    parent[i] = j
            if dp[i]>res: res = dp[i]

        ans = []
        for i in range(n):
            if dp[i]==res:
                while i!=-1:
                    ans.append(words[i])
                    i = parent[i]
                break
            
        return ans[::-1]
