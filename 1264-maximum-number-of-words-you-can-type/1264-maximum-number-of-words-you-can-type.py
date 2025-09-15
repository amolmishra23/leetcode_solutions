class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        res = 0

        for word in text.split():
            res += int(not any(ch in brokenLetters for ch in word))

        return res
