class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word[1:].islower() or word.isupper()