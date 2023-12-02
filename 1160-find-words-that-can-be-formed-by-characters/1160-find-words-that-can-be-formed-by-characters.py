class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        return sum([len(word) if all(co<=count[ch] for ch, co in Counter(word).items()) else 0 for word in words])
            
        