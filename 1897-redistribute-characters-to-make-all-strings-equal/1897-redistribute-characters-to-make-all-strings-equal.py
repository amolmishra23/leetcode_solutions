class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(v%len(words)==0 for v in Counter("".join(words)).values())