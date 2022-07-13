class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        valid = set([""])
       
        for word in sorted(words, key=lambda x: len(x)):
           if word[:-1] in valid:
                valid.add(word)
								
        return max(sorted(valid), key=lambda x: len(x))