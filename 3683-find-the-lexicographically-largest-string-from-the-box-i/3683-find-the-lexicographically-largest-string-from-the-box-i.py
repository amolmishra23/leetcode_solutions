class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word

        res, n = "", len(word)
        k = n - numFriends + 1
        
        for i in range(len(word)):
            res = max(res, word[i:i+k])

        return res