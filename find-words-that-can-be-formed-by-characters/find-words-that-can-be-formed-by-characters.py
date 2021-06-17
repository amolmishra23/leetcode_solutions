class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        res=0
        
        for word in words:
            word_count = Counter(word)
            if all(word_count[x]<=char_count[x] for x in word_count): res+=len(word)
        
        return res