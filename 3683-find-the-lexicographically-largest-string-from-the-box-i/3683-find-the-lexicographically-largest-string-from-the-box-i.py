class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word

        res, n = "", len(word)

        for i in range(len(word)):
            k = min(n - i, n - numFriends + 1)
            res = max(res, word[i:i+k])

        return res