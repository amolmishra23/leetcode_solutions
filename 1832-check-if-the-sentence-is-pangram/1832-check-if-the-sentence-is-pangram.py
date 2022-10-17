class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(string.ascii_letters[:26]) == set(sentence) 