class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        words.append(words[0])
        return all(x[-1]==y[0] for x,y in zip(words[:-1], words[1:]))
        