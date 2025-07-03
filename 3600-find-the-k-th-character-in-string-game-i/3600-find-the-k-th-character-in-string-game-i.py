class Solution:
    def getNext(self, word):
        new = [(ch+1)%26 for ch in word]
        return word+new

    def kthCharacter(self, k: int) -> str:
        word = [0]
        while len(word)<k: word = self.getNext(word)
        return chr(word[k-1]+ord("a"))